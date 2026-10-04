import re, os

ROOT = os.path.dirname(os.path.abspath(__file__))
PART = os.path.join(ROOT, "_partials")

with open(os.path.join(PART, "head.html"), encoding="utf-8") as f:
    HEAD = f.read()
with open(os.path.join(PART, "footer.html"), encoding="utf-8") as f:
    FOOTER = f.read()

ORG_SCHEMA = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Gwarmai Global Resources Limited",
  "alternateName": "GGR",
  "url": "https://gwarmaiglobal.com/",
  "logo": "https://gwarmaiglobal.com/assets/images/logo.png",
  "description": "Specialized development consulting firm delivering evidence-based, community-centred solutions for climate resilience, environmental management, ESG compliance and inclusive growth in Nigeria.",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "135, Dangwauro Layout Road",
    "addressRegion": "Kano State",
    "addressCountry": "NG"
  },
  "email": "ggresouces@gmail.com",
  "telephone": "+234-803-600-5151"
}
</script>"""

PAGES = [
    ("index",     "index.html",     "Gwarmai Global Resources Limited | Home",
     "GGR is a specialized development consulting firm in Kano, Nigeria, delivering evidence-based solutions for climate resilience, ESG compliance and inclusive growth.", ORG_SCHEMA),
    ("about",     "about.html",     "Gwarmai Global Resources Limited | About Us",
     "Learn about Gwarmai Global Resources Limited (GGR), a Kano-based development consulting firm and technical partner for climate, environment and ESG programmes.", ""),
    ("services",  "services.html",  "Gwarmai Global Resources Limited | Services",
     "Explore GGR's core services: disaster risk reduction, ESG and social impact assessment, agricultural value chains, gender and social inclusion, and monitoring and evaluation.", ""),
    ("expertise", "expertise.html", "Gwarmai Global Resources Limited | Expertise",
     "GGR's technical expertise spans climate adaptation, ESG safeguards, agricultural value chains, social inclusion, and geospatial monitoring and evaluation across Nigeria.", ""),
    ("projects",  "projects.html",  "Gwarmai Global Resources Limited | Projects",
     "Selected GGR engagements including the Green Legacy technical partnership and the Kano-Maradi railway social impact assessment for Mota-Engil.", ""),
    ("approach",  "approach.html",  "Gwarmai Global Resources Limited | Our Approach",
     "GGR's programme approach: baseline and vulnerability assessment, design, implementation support, monitoring and evaluation, and knowledge documentation.", ""),
    ("team",      "team.html",      "Gwarmai Global Resources Limited | Team",
     "Meet GGR's key expert team, led by Dr. Umar Saleh Anka, with specialists in climate policy, GIS, stakeholder engagement, and gender and social inclusion.", ""),
    ("resources", "resources.html", "Gwarmai Global Resources Limited | Resources",
     "Download GGR's official company profile and access other documents and publications.", ""),
    ("contact",   "contact.html",   "Gwarmai Global Resources Limited | Contact",
     "Contact Gwarmai Global Resources Limited in Kano, Nigeria, by phone, WhatsApp, email, or the contact form.", ""),
    ("privacy",   "privacy.html",   "Gwarmai Global Resources Limited | Privacy Policy",
     "Privacy policy information for the Gwarmai Global Resources Limited website.", ""),
    ("404",       "404.html",       "Page Not Found | Gwarmai Global Resources Limited",
     "The page you're looking for could not be found on the Gwarmai Global Resources Limited website.", ""),
]

for key, path, title, desc, schema in PAGES:
    body_path = os.path.join(PART, f"body_{key}.html")
    with open(body_path, encoding="utf-8") as f:
        body = f.read()
    head = HEAD.replace("{{TITLE}}", title).replace("{{DESC}}", desc).replace("{{PATH}}", path).replace("{{SCHEMA}}", schema)
    html = head + "\n" + body + "\n" + FOOTER
    out_path = os.path.join(ROOT, path)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", out_path)
