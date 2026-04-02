from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch

def create_resume(filename):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    # === COLORS & STYLES ===
    navy = colors.HexColor("#0C1A3E")
    yellow = colors.HexColor("#F6C90E")
    grey = colors.HexColor("#555555")

    # === LEFT PANEL ===
    c.setFillColor(navy)
    c.rect(0, 0, 2.5 * inch, height, stroke=0, fill=1)

    # PROFILE IMAGE PLACEHOLDER
    c.setFillColor(colors.white)
    c.circle(1.25 * inch, height - 1.25 * inch, 0.6 * inch, stroke=0, fill=1)
    c.setFillColor(navy)
    c.setFont("Helvetica-Bold", 8)
    c.drawCentredString(1.25 * inch, height - 1.3 * inch, "Your Photo")

    # CONTACT SECTION
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(0.5 * inch, height - 2.2 * inch, "CONTACT")

    c.setFont("Helvetica", 9)
    contact_y = height - 2.5 * inch
    contact_details = [
        "+91 9025473647",
        "Pune, INDIA",
        "rajakumarhinchageri87@gmail.com",
        "3 Years 10 Months of experience"
    ]
    for line in contact_details:
        c.drawString(0.5 * inch, contact_y, line)
        contact_y -= 0.25 * inch

    # EDUCATION
    c.setFont("Helvetica-Bold", 11)
    c.drawString(0.5 * inch, contact_y - 0.3 * inch, "EDUCATION")

    c.setFont("Helvetica", 9)
    edu_y = contact_y - 0.6 * inch
    education = [
        ("2021", "B.Tech/BE – Computers\nVisvesvaraya Technological University"),
        ("2021", "XIIth – CBSE, English, Marks: 86%"),
        ("2019", "Xth – CBSE, English, Marks: 80%")
    ]
    for year, detail in education:
        c.setFont("Helvetica-Bold", 9)
        c.drawString(0.5 * inch, edu_y, year)
        edu_y -= 0.2 * inch
        c.setFont("Helvetica", 9)
        for line in detail.split("\n"):
            c.drawString(0.5 * inch, edu_y, line)
            edu_y -= 0.2 * inch
        edu_y -= 0.2 * inch

    # SKILLS
    c.setFont("Helvetica-Bold", 11)
    c.drawString(0.5 * inch, edu_y - 0.2 * inch, "KEY SKILLS")
    skills_y = edu_y - 0.5 * inch
    c.setFont("Helvetica", 9)
    skills = [
        "Spring Data JPA", "Tortoise SVN", "Git", "Microservices", 
        "Spring MVC", "Spring Boot", "MySQL", "Agile Methodology"
    ]
    for skill in skills:
        c.drawString(0.5 * inch, skills_y, f"- {skill}")
        skills_y -= 0.2 * inch

    # === RIGHT PANEL ===
    right_x = 3 * inch

    # NAME SECTION
    c.setFillColor(yellow)
    c.rect(right_x, height - 1.5 * inch, width - right_x, 1.5 * inch, stroke=0, fill=1)
    c.setFillColor(navy)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(right_x + 0.3 * inch, height - 0.8 * inch, "RAJAKUMAR")
    c.setFont("Helvetica", 14)
    c.drawString(right_x + 0.3 * inch, height - 1.1 * inch, "HINCHAGERI")
    c.setFont("Helvetica-Oblique", 10)
    c.setFillColor(colors.black)
    c.drawString(right_x + 0.3 * inch, height - 1.3 * inch, "SOFTWARE ENGINEER")

    # PROFILE SUMMARY
    c.setFillColor(yellow)
    c.circle(right_x + 0.1 * inch, height - 2.1 * inch, 0.05 * inch, stroke=0, fill=1)
    c.setFillColor(navy)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(right_x + 0.25 * inch, height - 2.2 * inch, "PROFILE SUMMARY")

    summary_text = (
        "Java Backend Developer with 3.10 years of experience in designing and developing scalable, "
        "secure, and high-performance applications. Skilled in Spring Boot, Microservices, and MySQL. "
        "Proven expertise in automation, diagnostics, and system optimization. Delivered 100% rule "
        "coverage in DDX testing and improved delivery by 15% through clean code and process automation."
    )

    text_obj = c.beginText()
    text_obj.setTextOrigin(right_x + 0.3 * inch, height - 2.6 * inch)
    text_obj.setFont("Helvetica", 10)
    text_obj.setFillColor(grey)
    text_obj.textLines(summary_text)
    c.drawText(text_obj)

    # WORK EXPERIENCE
    c.setFillColor(yellow)
    c.circle(right_x + 0.1 * inch, height - 4.7 * inch, 0.05 * inch, stroke=0, fill=1)
    c.setFillColor(navy)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(right_x + 0.25 * inch, height - 4.8 * inch, "WORK EXPERIENCE")

    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(colors.black)
    c.drawString(right_x + 0.3 * inch, height - 5.2 * inch, "2021 - Present")
    c.drawString(right_x + 1.3 * inch, height - 5.2 * inch, "Software Engineer - KPIT")

    exp_text = (
        "Experienced in building scalable, secure, and high-performance backend applications "
        "using Spring Boot, Microservices, and MySQL. Proven expertise in automation, diagnostics, "
        "and system optimization."
    )

    text_obj = c.beginText()
    text_obj.setTextOrigin(right_x + 0.3 * inch, height - 5.5 * inch)
    text_obj.setFont("Helvetica", 10)
    text_obj.setFillColor(grey)
    text_obj.textLines(exp_text)
    c.drawText(text_obj)

    c.showPage()
    c.save()
    print(f"✅ Resume PDF created: {filename}")

create_resume("Rajakumar_Resume.pdf")
