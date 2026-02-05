from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY

def create_insurance_policy_pdf(path="data/knowledge.pdf"):
    """
    Creates a comprehensive insurance policy document with detailed coverage information.
    This PDF will serve as the knowledge base for your RAG system.
    """
    
    doc = SimpleDocTemplate(path, pagesize=letter,
                           topMargin=0.75*inch, bottomMargin=0.75*inch)
    
    # Get default styles
    styles = getSampleStyleSheet()
    
    # Create custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=18,
        textColor=colors.HexColor('#1a365d'),
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor('#2d3748'),
        spaceAfter=12,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )
    
    subheading_style = ParagraphStyle(
        'CustomSubHeading',
        parent=styles['Heading3'],
        fontSize=12,
        textColor=colors.HexColor('#4a5568'),
        spaceAfter=8,
        spaceBefore=8,
        fontName='Helvetica-Bold'
    )
    
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=10,
        alignment=TA_JUSTIFY,
        spaceAfter=12
    )
    
    # Build the document content
    story = []
    
    # Title Page
    story.append(Spacer(1, 1*inch))
    story.append(Paragraph("COMPREHENSIVE INSURANCE POLICY", title_style))
    story.append(Paragraph("Policy Number: INS-2025-847392", styles['Normal']))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("Secure Life Insurance Company", styles['Heading2']))
    story.append(Paragraph("Effective Date: January 1, 2025", styles['Normal']))
    story.append(Paragraph("Policy Period: 12 Months", styles['Normal']))
    story.append(PageBreak())
    
    # Table of Contents
    story.append(Paragraph("TABLE OF CONTENTS", heading_style))
    story.append(Spacer(1, 0.2*inch))
    
    toc_items = [
        "1. Policy Overview",
        "2. Coverage Details",
        "3. Exclusions and Limitations",
        "4. Premium Information",
        "5. Claims Process",
        "6. Customer Service",
        "7. Cancellation Policy",
        "8. Renewal Terms"
    ]
    
    for item in toc_items:
        story.append(Paragraph(item, body_style))
    
    story.append(PageBreak())
    
    # Section 1: Policy Overview
    story.append(Paragraph("1. POLICY OVERVIEW", heading_style))
    
    story.append(Paragraph("""
    This Comprehensive Insurance Policy provides extensive coverage for health, life, and property protection. 
    Our policy is designed to give you peace of mind by protecting you and your family against unexpected events. 
    This document outlines all coverage details, terms, conditions, and procedures for filing claims.
    """, body_style))
    
    story.append(Paragraph("Policy Holder Information", subheading_style))
    story.append(Paragraph("""
    This policy covers the primary policyholder and eligible dependents as listed in your policy schedule. 
    Dependents include spouse, children under 26 years of age, and other family members specifically added to the policy. 
    Each covered individual receives the full benefits outlined in this document.
    """, body_style))
    
    story.append(PageBreak())
    
    # Section 2: Coverage Details
    story.append(Paragraph("2. COVERAGE DETAILS", heading_style))
    
    # Health Coverage
    story.append(Paragraph("2.1 Health Insurance Coverage", subheading_style))
    
    story.append(Paragraph("""
    Our health insurance provides comprehensive medical coverage including hospitalization, outpatient services, 
    prescription medications, preventive care, and emergency services.
    """, body_style))
    
    # Create coverage table
    coverage_data = [
        ['Service Type', 'Coverage Amount', 'Deductible', 'Co-pay'],
        ['Hospital Stay (per day)', '$1,500', '$500', '20%'],
        ['Emergency Room Visit', '$2,000', '$200', '15%'],
        ['Doctor Office Visit', '$150', '$0', '$25'],
        ['Specialist Visit', '$250', '$0', '$50'],
        ['Prescription Drugs (Generic)', '100%', '$0', '$10'],
        ['Prescription Drugs (Brand)', '80%', '$0', '$35'],
        ['Preventive Care', '100%', '$0', '$0'],
        ['Laboratory Tests', '100%', '$100', '10%'],
        ['X-Rays and Imaging', '90%', '$150', '10%'],
        ['Surgery (Inpatient)', 'Up to $50,000', '$1,000', '20%']
    ]
    
    coverage_table = Table(coverage_data, colWidths=[2.2*inch, 1.5*inch, 1.2*inch, 1*inch])
    coverage_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2d3748')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f7fafc')])
    ]))
    
    story.append(coverage_table)
    story.append(Spacer(1, 0.3*inch))
    
    # Life Insurance
    story.append(Paragraph("2.2 Life Insurance Coverage", subheading_style))
    
    story.append(Paragraph("""
    The life insurance component provides financial protection for your beneficiaries in the event of your death. 
    Coverage amount: $500,000. This includes accidental death benefit of an additional $250,000 if death occurs 
    due to an accident. The policy also includes a terminal illness rider allowing access to 50% of the death 
    benefit if diagnosed with a terminal illness with less than 12 months to live.
    """, body_style))
    
    # Property Coverage
    story.append(Paragraph("2.3 Property Insurance Coverage", subheading_style))
    
    story.append(Paragraph("""
    Property coverage protects your home and personal belongings against loss or damage from covered perils 
    including fire, theft, vandalism, weather damage, and natural disasters. Dwelling coverage: $350,000. 
    Personal property coverage: $175,000 (50% of dwelling coverage). Additional living expenses: $70,000 
    if your home becomes uninhabitable due to a covered loss.
    """, body_style))
    
    story.append(PageBreak())
    
    # Section 3: Exclusions
    story.append(Paragraph("3. EXCLUSIONS AND LIMITATIONS", heading_style))
    
    story.append(Paragraph("""
    This policy does not cover the following situations and conditions. Please review these exclusions 
    carefully to understand the limits of your coverage.
    """, body_style))
    
    story.append(Paragraph("3.1 Health Insurance Exclusions", subheading_style))
    
    exclusions = [
        "Cosmetic surgery or procedures not medically necessary",
        "Experimental or investigational treatments",
        "Self-inflicted injuries",
        "Injuries resulting from illegal activities",
        "Pre-existing conditions (coverage begins after 6-month waiting period)",
        "Dental care except for accident-related injuries",
        "Vision care (regular eye exams and glasses)",
        "Fertility treatments and surrogacy",
        "Weight loss programs unless medically necessary"
    ]
    
    for exclusion in exclusions:
        story.append(Paragraph(f"• {exclusion}", body_style))
    
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("3.2 Life Insurance Exclusions", subheading_style))
    
    life_exclusions = [
        "Death by suicide within the first 2 years of policy",
        "Death while committing a felony",
        "Death during war or military conflict (unless military rider purchased)",
        "Death from aviation activities (unless commercial airline passenger)"
    ]
    
    for exclusion in life_exclusions:
        story.append(Paragraph(f"• {exclusion}", body_style))
    
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("3.3 Property Insurance Exclusions", subheading_style))
    
    property_exclusions = [
        "Flood damage (separate flood insurance required)",
        "Earthquake damage (separate earthquake insurance required)",
        "Normal wear and tear",
        "Pest or rodent damage",
        "Intentional damage by the policyholder",
        "Nuclear hazard",
        "Government action (eminent domain, seizure)"
    ]
    
    for exclusion in property_exclusions:
        story.append(Paragraph(f"• {exclusion}", body_style))
    
    story.append(PageBreak())
    
    # Section 4: Premium Information
    story.append(Paragraph("4. PREMIUM INFORMATION", heading_style))
    
    story.append(Paragraph("""
    Your premium is the amount you pay to maintain active coverage under this policy. Premium amounts are 
    calculated based on coverage levels, age, location, and other risk factors.
    """, body_style))
    
    story.append(Paragraph("4.1 Premium Amounts", subheading_style))
    
    premium_data = [
        ['Coverage Type', 'Monthly Premium', 'Annual Premium'],
        ['Health Insurance', '$450', '$5,100'],
        ['Life Insurance', '$75', '$850'],
        ['Property Insurance', '$125', '$1,425'],
        ['Total Premium', '$650', '$7,375']
    ]
    
    premium_table = Table(premium_data, colWidths=[2.5*inch, 1.8*inch, 1.8*inch])
    premium_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2d3748')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor('#edf2f7')),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTSIZE', (0, 1), (-1, -1), 9)
    ]))
    
    story.append(premium_table)
    story.append(Spacer(1, 0.3*inch))
    
    story.append(Paragraph("4.2 Payment Options", subheading_style))
    
    story.append(Paragraph("""
    Premiums can be paid monthly, quarterly, semi-annually, or annually. Annual payment receives a 5% discount. 
    Payment methods include automatic bank draft, credit card, debit card, or check. A 30-day grace period is 
    provided for late payments. If payment is not received within the grace period, coverage will be suspended.
    """, body_style))
    
    story.append(Paragraph("4.3 Deductibles Explained", subheading_style))
    
    story.append(Paragraph("""
    A deductible is the amount you must pay out-of-pocket before your insurance coverage begins to pay. 
    For example, if you have a $500 deductible for hospital stays and your bill is $3,000, you pay the first 
    $500 and the insurance covers the remaining $2,500 (subject to co-insurance). Deductibles reset annually 
    on your policy anniversary date. Family deductibles are typically 2-3 times the individual deductible.
    """, body_style))
    
    story.append(PageBreak())
    
    # Section 5: Claims Process
    story.append(Paragraph("5. CLAIMS PROCESS", heading_style))
    
    story.append(Paragraph("""
    Filing a claim is straightforward. Follow these steps to ensure quick processing and payment of your claim.
    """, body_style))
    
    story.append(Paragraph("5.1 How to File a Claim", subheading_style))
    
    claim_steps = [
        "<b>Step 1: Notify Us Immediately</b><br/>Contact our claims department within 24 hours of the incident. Call our 24/7 claims hotline at 1-800-CLAIMS-1 (1-800-252-4671) or file online at www.securelife.com/claims",
        
        "<b>Step 2: Gather Documentation</b><br/>Collect all relevant documents including medical bills, police reports (for theft or accidents), repair estimates, photos of damage, and receipts. Keep copies of everything for your records.",
        
        "<b>Step 3: Complete Claim Form</b><br/>Fill out the appropriate claim form available on our website or request one from our claims department. Provide detailed information about the incident, date, time, location, and circumstances.",
        
        "<b>Step 4: Submit Your Claim</b><br/>Submit your completed claim form and supporting documents via:<br/>• Online portal: www.securelife.com/claims<br/>• Email: claims@securelife.com<br/>• Fax: 1-888-555-0199<br/>• Mail: Secure Life Insurance, Claims Department, PO Box 12345, New York, NY 10001",
        
        "<b>Step 5: Claim Review Process</b><br/>Our claims adjuster will review your submission within 3-5 business days. We may contact you for additional information or documentation. You'll receive a claim number for tracking purposes.",
        
        "<b>Step 6: Claim Decision</b><br/>Most claims are processed within 10-15 business days. You'll receive written notification of our decision. If approved, payment will be issued within 5 business days via direct deposit or check."
    ]
    
    for step in claim_steps:
        story.append(Paragraph(step, body_style))
        story.append(Spacer(1, 0.1*inch))
    
    story.append(Paragraph("5.2 Required Documentation by Claim Type", subheading_style))
    
    doc_requirements = [
        "<b>Health Claims:</b> Itemized medical bills, diagnosis codes, treatment records, prescription receipts, referral forms (if applicable)",
        "<b>Life Claims:</b> Death certificate, beneficiary identification, policy documents, proof of relationship to deceased",
        "<b>Property Claims:</b> Photos/videos of damage, repair estimates (minimum 2), police report (for theft/vandalism), proof of ownership for valuable items"
    ]
    
    for req in doc_requirements:
        story.append(Paragraph(req, body_style))
    
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("5.3 Claim Status and Appeals", subheading_style))
    
    story.append(Paragraph("""
    You can check your claim status 24/7 online at www.securelife.com/claim-status or by calling 1-800-252-4671. 
    If your claim is denied, you have the right to appeal. Submit a written appeal within 60 days of the denial 
    notice. Include any additional documentation that supports your claim. Appeals are reviewed by a different 
    adjuster and you'll receive a decision within 30 days.
    """, body_style))
    
    story.append(PageBreak())
    
    # Section 6: Customer Service
    story.append(Paragraph("6. CUSTOMER SERVICE AND SUPPORT", heading_style))
    
    story.append(Paragraph("""
    We're here to help you with any questions or concerns about your policy. Our customer service team is 
    dedicated to providing exceptional support.
    """, body_style))
    
    story.append(Paragraph("6.1 Contact Information", subheading_style))
    
    contact_info = [
        "<b>Customer Service Hours:</b><br/>Monday - Friday: 8:00 AM - 8:00 PM EST<br/>Saturday: 9:00 AM - 5:00 PM EST<br/>Sunday: Closed (emergency claims only)",
        "<b>Phone Numbers:</b><br/>General Inquiries: 1-800-555-0123<br/>Claims: 1-800-252-4671 (24/7)<br/>Billing: 1-800-555-0145<br/>Spanish: 1-800-555-0156",
        "<b>Online Services:</b><br/>Website: www.securelife.com<br/>Email: support@securelife.com<br/>Live Chat: Available on website during business hours<br/>Mobile App: Download 'Secure Life' on iOS or Android",
        "<b>Mailing Address:</b><br/>Secure Life Insurance Company<br/>Customer Service Department<br/>123 Insurance Plaza<br/>New York, NY 10001"
    ]
    
    for info in contact_info:
        story.append(Paragraph(info, body_style))
        story.append(Spacer(1, 0.15*inch))
    
    story.append(Paragraph("6.2 Common Questions", subheading_style))
    
    faqs = [
        ("<b>How do I add a dependent to my policy?</b>", 
         "Contact customer service within 30 days of a qualifying life event (marriage, birth, adoption). Provide dependent's information and necessary documentation. Coverage begins the first of the month following approval."),
        
        ("<b>Can I change my coverage levels?</b>", 
         "Yes, during open enrollment (November 1-30) or within 30 days of a qualifying life event. Changes take effect the following month. Some changes may require medical underwriting."),
        
        ("<b>What happens if I miss a payment?</b>", 
         "You have a 30-day grace period. Coverage continues during this time. If payment isn't received, policy will lapse. Reinstatement requires back payment plus a $50 reinstatement fee."),
        
        ("<b>How do I update my beneficiaries?</b>", 
         "Complete a beneficiary change form online or call customer service. Changes are effective upon receipt and processing. We recommend reviewing beneficiaries annually."),
        
        ("<b>Is there a waiting period for coverage?</b>", 
         "Health coverage begins immediately for accidents. Illness coverage has a 14-day waiting period. Pre-existing conditions have a 6-month waiting period. Life and property coverage begin on policy effective date.")
    ]
    
    for question, answer in faqs:
        story.append(Paragraph(question, body_style))
        story.append(Paragraph(answer, body_style))
        story.append(Spacer(1, 0.1*inch))
    
    story.append(PageBreak())
    
    # Section 7: Cancellation
    story.append(Paragraph("7. CANCELLATION POLICY", heading_style))
    
    story.append(Paragraph("""
    Either party may cancel this policy subject to the terms and conditions outlined below. We value your 
    business and hope to retain you as a customer.
    """, body_style))
    
    story.append(Paragraph("7.1 Cancellation by Policyholder", subheading_style))
    
    story.append(Paragraph("""
    You may cancel your policy at any time by providing written notice. Send cancellation request via email 
    to cancellations@securelife.com or mail to our customer service address. Cancellation takes effect 30 days 
    from receipt of notice or on a date you specify (whichever is later). You'll receive a pro-rated refund 
    for any unused premium, minus a $25 processing fee. No refund is issued if claims were paid during the 
    current policy period.
    """, body_style))
    
    story.append(Paragraph("7.2 Cancellation by Company", subheading_style))
    
    story.append(Paragraph("""
    We may cancel your policy for the following reasons: non-payment of premium, fraud or material 
    misrepresentation, substantial increase in risk, or loss of required license. We'll provide 30 days 
    written notice before cancellation (10 days for non-payment). You'll receive a full refund of unearned 
    premium with no processing fee if we initiate cancellation.
    """, body_style))
    
    story.append(PageBreak())
    
    # Section 8: Renewal
    story.append(Paragraph("8. RENEWAL TERMS", heading_style))
    
    story.append(Paragraph("""
    This policy automatically renews annually unless you notify us otherwise. Renewal terms and conditions 
    are outlined below.
    """, body_style))
    
    story.append(Paragraph("8.1 Automatic Renewal", subheading_style))
    
    story.append(Paragraph("""
    Your policy will automatically renew on your anniversary date. We'll send a renewal notice 60 days before 
    expiration showing any changes to coverage or premium. Premium increases are based on age, claims history, 
    inflation, and market conditions. You have 30 days from receipt of renewal notice to decline renewal 
    without penalty.
    """, body_style))
    
    story.append(Paragraph("8.2 Policy Updates at Renewal", subheading_style))
    
    story.append(Paragraph("""
    At renewal, we may update policy terms to comply with new regulations or adjust coverage limits. 
    Significant changes require your written acceptance. If you don't agree with changes, you may decline 
    renewal and we'll provide a 60-day extension at current terms to allow time to find alternative coverage.
    """, body_style))
    
    story.append(Spacer(1, 0.5*inch))
    
    # Final Section
    story.append(Paragraph("IMPORTANT NOTICE", heading_style))
    
    story.append(Paragraph("""
    This policy represents the entire agreement between you and Secure Life Insurance Company. No agent or 
    representative can modify this policy or waive any of its provisions. All modifications must be in writing 
    and signed by an authorized company officer. Please keep this policy in a safe place and review it annually 
    to ensure it continues to meet your needs.
    """, body_style))
    
    story.append(Spacer(1, 0.3*inch))
    
    story.append(Paragraph("""
    For questions or concerns, please contact our customer service team. We're committed to providing you 
    with excellent service and comprehensive protection.
    """, body_style))
    
    story.append(Spacer(1, 0.5*inch))
    
    story.append(Paragraph("Thank you for choosing Secure Life Insurance Company.", 
                          ParagraphStyle('Final', parent=styles['Normal'], 
                                       fontSize=11, fontName='Helvetica-Bold', alignment=TA_CENTER)))
    
    # Build the PDF
    doc.build(story)
    print(f"✓ Insurance policy PDF created successfully at: {path}")
    print(f"✓ Document contains comprehensive coverage information for RAG system")

if __name__ == "__main__":
    create_insurance_policy_pdf()