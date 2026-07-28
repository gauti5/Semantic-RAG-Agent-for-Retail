"""
Generate a 25-page Retail Display Manual PDF for the RAG Agent project.
Simulates a real CPG/Retail merchandising SOP document.
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black, white
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, ListFlowable, ListItem, KeepTogether
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "Data")
os.makedirs(OUTPUT_DIR, exist_ok=True)
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "Retail_Display_Manual.pdf")

# Custom colors
BRAND_BLUE = HexColor("#1B3A6B")
BRAND_ORANGE = HexColor("#E87722")
LIGHT_GRAY = HexColor("#F2F2F2")
MEDIUM_GRAY = HexColor("#CCCCCC")


def get_styles():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name='CoverTitle', fontSize=28, leading=34, alignment=TA_CENTER,
        textColor=BRAND_BLUE, spaceAfter=20, fontName='Helvetica-Bold'
    ))
    styles.add(ParagraphStyle(
        name='CoverSubtitle', fontSize=14, leading=18, alignment=TA_CENTER,
        textColor=BRAND_ORANGE, spaceAfter=40, fontName='Helvetica'
    ))
    styles.add(ParagraphStyle(
        name='ChapterTitle', fontSize=20, leading=24, textColor=BRAND_BLUE,
        spaceAfter=12, spaceBefore=20, fontName='Helvetica-Bold'
    ))
    styles.add(ParagraphStyle(
        name='SectionTitle', fontSize=14, leading=18, textColor=BRAND_BLUE,
        spaceAfter=8, spaceBefore=14, fontName='Helvetica-Bold'
    ))
    styles.add(ParagraphStyle(
        name='SubSection', fontSize=12, leading=15, textColor=black,
        spaceAfter=6, spaceBefore=10, fontName='Helvetica-Bold'
    ))
    styles.add(ParagraphStyle(
        name='BodyText2', fontSize=10, leading=14, alignment=TA_JUSTIFY,
        spaceAfter=8, fontName='Helvetica'
    ))
    styles.add(ParagraphStyle(
        name='TableHeader', fontSize=9, leading=12, alignment=TA_CENTER,
        textColor=white, fontName='Helvetica-Bold'
    ))
    styles.add(ParagraphStyle(
        name='TableCell', fontSize=9, leading=12, alignment=TA_LEFT,
        fontName='Helvetica'
    ))
    styles.add(ParagraphStyle(
        name='Footer', fontSize=8, leading=10, alignment=TA_CENTER,
        textColor=MEDIUM_GRAY
    ))
    styles.add(ParagraphStyle(
        name='Warning', fontSize=10, leading=14, alignment=TA_LEFT,
        textColor=HexColor("#CC0000"), fontName='Helvetica-Bold', spaceAfter=8
    ))
    return styles


def build_cover_page(story, styles):
    story.append(Spacer(1, 2 * inch))
    story.append(Paragraph("RETAIL DISPLAY MANUAL", styles['CoverTitle']))
    story.append(Paragraph("Standard Operating Procedures &<br/>Merchandising Guidelines", styles['CoverSubtitle']))
    story.append(Spacer(1, 0.5 * inch))
    story.append(Paragraph("FreshMart Global Retail Corporation", styles['CoverSubtitle']))
    story.append(Spacer(1, 1 * inch))

    cover_info = [
        ["Document ID:", "FM-SOP-2025-001"],
        ["Version:", "4.2"],
        ["Effective Date:", "January 15, 2025"],
        ["Review Date:", "July 15, 2025"],
        ["Classification:", "INTERNAL - Store Operations"],
        ["Department:", "Visual Merchandising & Store Standards"],
    ]
    t = Table(cover_info, colWidths=[2 * inch, 3 * inch])
    t.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ]))
    story.append(t)
    story.append(Spacer(1, 1.5 * inch))
    story.append(Paragraph("CONFIDENTIAL — For authorized store personnel only.", styles['Footer']))
    story.append(PageBreak())


def build_toc(story, styles):
    story.append(Paragraph("TABLE OF CONTENTS", styles['ChapterTitle']))
    story.append(Spacer(1, 0.3 * inch))
    chapters = [
        ("1. Introduction & Scope", "3"),
        ("2. General Store Layout Standards", "4"),
        ("3. Shelf Planogram Guidelines", "6"),
        ("4. End-Cap & Promotional Display Setup", "8"),
        ("5. Beverage Aisle Standards", "10"),
        ("6. Fresh Produce Display Requirements", "12"),
        ("7. Frozen Foods Merchandising", "14"),
        ("8. Safety & Compliance Protocols", "16"),
        ("9. Seasonal & Holiday Displays", "18"),
        ("10. Digital Signage & Price Tag Standards", "20"),
        ("11. Audit Checklists & Scoring", "22"),
        ("12. Appendix: Quick Reference Cards", "24"),
    ]
    toc_data = [["Chapter", "Page"]] + [[c, p] for c, p in chapters]
    t = Table(toc_data, colWidths=[4.5 * inch, 1 * inch])
    t.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('LINEBELOW', (0, 0), (-1, 0), 1, BRAND_BLUE),
        ('LINEBELOW', (0, 1), (-1, -1), 0.5, MEDIUM_GRAY),
        ('ALIGN', (1, 0), (1, -1), 'CENTER'),
    ]))
    story.append(t)
    story.append(PageBreak())


def build_chapter1(story, styles):
    story.append(Paragraph("1. Introduction & Scope", styles['ChapterTitle']))
    story.append(Paragraph("1.1 Purpose", styles['SectionTitle']))
    story.append(Paragraph(
        "This Retail Display Manual establishes the standard operating procedures (SOPs) for all "
        "FreshMart Global store locations. It provides comprehensive guidelines for product placement, "
        "visual merchandising, promotional displays, and safety compliance. All store managers, "
        "assistant managers, and merchandising associates are required to follow these procedures "
        "to ensure brand consistency and optimal customer experience across all 2,400+ locations.",
        styles['BodyText2']
    ))
    story.append(Paragraph(
        "The manual is organized into twelve chapters covering every aspect of in-store merchandising "
        "from general layout principles to specific department standards. Each chapter includes "
        "actionable guidelines, measurement criteria, and reference tables. Associates should treat "
        "this document as the single source of truth for all visual merchandising decisions. When "
        "conflicts arise between this manual and vendor-supplied materials, this manual takes precedence "
        "unless a written exception has been granted by the VP of Merchandising.",
        styles['BodyText2']
    ))
    story.append(Paragraph("1.2 Scope of Application", styles['SectionTitle']))
    story.append(Paragraph(
        "These guidelines apply to all FreshMart store formats including: Hypermarkets (40,000+ sq ft), "
        "Supermarkets (15,000-40,000 sq ft), Express stores (3,000-15,000 sq ft), and Neighborhood "
        "Markets (under 3,000 sq ft). Store format-specific exceptions are noted where applicable.",
        styles['BodyText2']
    ))
    story.append(Paragraph(
        "For Hypermarket format stores, additional guidelines apply to the General Merchandise (GM) "
        "sections including apparel, electronics, and home goods. These supplementary guidelines are "
        "published in the GM Merchandising Addendum (FM-SOP-2025-002) and should be read in conjunction "
        "with this manual. Express format stores may apply the 'Express Exception Protocol' (Section 1.5) "
        "which permits reduced facing counts and condensed promotional display footprints where space "
        "constraints exist. All exceptions must be documented in StoreConnect.",
        styles['BodyText2']
    ))
    story.append(Paragraph("1.3 Compliance Requirements", styles['SectionTitle']))
    items = [
        "All displays must be set within 24 hours of receiving new planogram directives.",
        "Weekly compliance audits are mandatory for all store formats.",
        "Non-compliance on critical safety items results in immediate corrective action.",
        "Photographic evidence of display execution must be uploaded to the StoreConnect app within 4 hours of completion.",
        "Regional managers conduct monthly spot-checks with a minimum score of 85% required.",
    ]
    for item in items:
        story.append(Paragraph(f"• {item}", styles['BodyText2']))
    story.append(Paragraph("1.4 Roles & Responsibilities", styles['SectionTitle']))
    roles_data = [
        ["Role", "Merchandising Responsibilities", "Audit Frequency"],
        ["Store Manager", "Overall compliance owner; approves display changes; signs off on weekly audit", "Reviews daily"],
        ["Asst. Store Manager", "Executes weekly self-audit; manages display setup crew", "Weekly WMSA"],
        ["Dept. Manager", "Department planogram compliance; product rotation; signage accuracy", "Daily zone walk"],
        ["Merch Associate", "Physical execution of planograms; display builds; restocking", "Shift-level tasks"],
        ["Regional Coordinator", "Monthly audits; corrective action oversight; training delivery", "Monthly visit"],
        ["Category Manager", "Planogram design; facing allocation; promotional strategy", "Quarterly review"],
    ]
    t = Table(roles_data, colWidths=[1.3 * inch, 3.2 * inch, 1.5 * inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), BRAND_BLUE),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, MEDIUM_GRAY),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, LIGHT_GRAY]),
    ]))
    story.append(t)
    story.append(Spacer(1, 0.2 * inch))
    story.append(Paragraph("1.5 Training Requirements", styles['SectionTitle']))
    story.append(Paragraph(
        "All new merchandising associates must complete the 'FreshMart Visual Standards Certification' "
        "(VSC) within 30 days of hire. The certification includes 8 hours of classroom training, "
        "4 hours of hands-on planogram execution practice, and a written exam (passing score: 80%). "
        "Annual recertification is required for all associates. Department managers must additionally "
        "complete the 'Advanced Merchandising Leadership' (AML) module covering audit procedures, "
        "vendor management, and corrective action planning. Training records are maintained in "
        "the HR module of StoreConnect and are auditable by regional leadership.",
        styles['BodyText2']
    ))
    story.append(Paragraph("1.6 Document Revision History", styles['SectionTitle']))
    rev_data = [
        ["Version", "Date", "Changes", "Approved By"],
        ["4.2", "Jan 2025", "Updated seasonal display protocols, added digital signage section", "VP Merchandising"],
        ["4.1", "Sep 2024", "Revised safety protocols per OSHA update", "Safety Director"],
        ["4.0", "Mar 2024", "Major restructure; added fresh produce standards", "COO"],
        ["3.8", "Nov 2023", "Minor corrections to planogram section", "Regional Ops"],
    ]
    t = Table(rev_data, colWidths=[0.7 * inch, 0.9 * inch, 3.2 * inch, 1.4 * inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), BRAND_BLUE),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 0.5, MEDIUM_GRAY),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('BACKGROUND', (0, 1), (-1, -1), LIGHT_GRAY),
    ]))
    story.append(t)
    story.append(PageBreak())


def build_chapter2(story, styles):
    story.append(Paragraph("2. General Store Layout Standards", styles['ChapterTitle']))
    story.append(Paragraph("2.1 Traffic Flow Principles", styles['SectionTitle']))
    story.append(Paragraph(
        "Store layout must follow the counter-clockwise traffic flow model. Research indicates that "
        "72% of customers naturally turn right upon entry. The decompression zone (first 5-15 feet) "
        "must remain free of promotional materials to allow customers to orient themselves. Power walls "
        "(right-side displays upon entry) should feature high-margin seasonal items.",
        styles['BodyText2']
    ))
    story.append(Paragraph("2.2 Aisle Width Requirements", styles['SectionTitle']))
    aisle_data = [
        ["Aisle Type", "Minimum Width", "Preferred Width", "Max Display Height"],
        ["Primary Aisles", "8 feet", "10 feet", "6 feet"],
        ["Secondary Aisles", "6 feet", "8 feet", "5.5 feet"],
        ["Perimeter Aisles", "10 feet", "12 feet", "7 feet"],
        ["Checkout Lanes", "4 feet", "5 feet", "4 feet"],
        ["Emergency Exits", "6 feet", "8 feet", "No obstruction"],
    ]
    t = Table(aisle_data, colWidths=[1.8 * inch, 1.3 * inch, 1.3 * inch, 1.8 * inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), BRAND_BLUE),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 0.5, MEDIUM_GRAY),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, LIGHT_GRAY]),
    ]))
    story.append(t)
    story.append(Spacer(1, 0.2 * inch))
    story.append(Paragraph("2.3 Zone Designation System", styles['SectionTitle']))
    story.append(Paragraph(
        "Each store is divided into merchandising zones labeled A through F. Zone A represents "
        "the front-of-store power area (highest traffic). Zone B covers primary promotional end-caps. "
        "Zone C encompasses standard gondola shelving. Zone D designates the perimeter fresh departments. "
        "Zone E covers back-of-store destinations (dairy, meat). Zone F is reserved for seasonal "
        "flex space that changes based on promotional calendar.",
        styles['BodyText2']
    ))
    story.append(Paragraph("2.4 Fixture Placement Rules", styles['SectionTitle']))
    story.append(Paragraph(
        "All gondola fixtures must be anchored to the floor using approved base plates (Part #FM-BP-400). "
        "Free-standing displays over 4 feet tall require anti-tip brackets. Wing panels must not extend "
        "more than 18 inches into the aisle. Clip strips are limited to 6 per gondola section and must "
        "not block product facings. All fixtures must maintain 18 inches clearance from sprinkler heads "
        "per fire code requirements.",
        styles['BodyText2']
    ))
    story.append(Paragraph("2.5 Lighting Standards", styles['SectionTitle']))
    story.append(Paragraph(
        "General merchandise areas require minimum 50 foot-candles illumination. Fresh departments "
        "(produce, bakery, deli) require 70-80 foot-candles with color temperature of 3000K to enhance "
        "product appearance. Promotional end-caps should have accent lighting at 100+ foot-candles. "
        "Burnt-out bulbs must be replaced within 4 hours during operating hours. LED retrofits must "
        "maintain CRI (Color Rendering Index) of 90 or higher.",
        styles['BodyText2']
    ))
    story.append(Paragraph("2.6 Customer Sightline Management", styles['SectionTitle']))
    story.append(Paragraph(
        "Sightlines are the unobstructed visual pathways that allow customers to see deep into the "
        "store from the entrance. Primary sightlines must remain clear at all times — no promotional "
        "displays, floor stacks, or temporary fixtures may block the view from the entrance to the "
        "back wall. Secondary sightlines (cross-aisle views at main intersections) must maintain "
        "minimum 4-foot clear viewable width. Department signage (hanging signs) must be positioned "
        "at minimum 7.5 feet above floor level to remain visible above gondola tops. Power category "
        "signage (Bakery, Deli, Produce) uses illuminated blade signs at 8-foot mounting height.",
        styles['BodyText2']
    ))
    story.append(Paragraph("2.7 Floor Surface & Maintenance Standards", styles['SectionTitle']))
    story.append(Paragraph(
        "Store floors must be maintained to a high-gloss finish (minimum 70 gloss units on reflectometer). "
        "Auto-scrubbing is performed nightly between 10 PM and 5 AM. During operating hours, spot "
        "mopping is performed as needed. Floor tiles near cooler cases must be inspected hourly for "
        "condensation. Cracked or chipped tiles are reported to maintenance and repaired within 48 hours. "
        "Floor decals for promotional events must use approved low-residue adhesive (supplier: SignCo "
        "Part #SC-FR-100) and are removed within 24 hours of promotion end date. Floor striping for "
        "departments uses the following color code: Blue = Grocery, Green = Fresh, Red = Meat/Seafood, "
        "Yellow = Bakery/Deli, Gray = GM/HBC.",
        styles['BodyText2']
    ))
    story.append(Paragraph("2.8 Gondola End Panel Utilization", styles['SectionTitle']))
    story.append(Paragraph(
        "Gondola end panels (the narrow vertical surfaces at the end of each aisle) are premium "
        "advertising space. Allocation follows this priority: (1) Current weekly ad items, "
        "(2) Loyalty program exclusive offers, (3) New product launches (first 8 weeks), "
        "(4) Vendor-funded co-op advertising. Panel signs must be printed on approved card stock "
        "(minimum 14pt, UV-coated) and secured with magnetic strip holders. Hand-written signs "
        "are strictly prohibited on end panels visible to customers. Each panel accommodates one "
        "11x17 portrait-orientation sign. Rotation occurs every Monday morning by 8:00 AM.",
        styles['BodyText2']
    ))
    story.append(PageBreak())


def build_chapter3(story, styles):
    story.append(Paragraph("3. Shelf Planogram Guidelines", styles['ChapterTitle']))
    story.append(Paragraph("3.1 Planogram Compliance Overview", styles['SectionTitle']))
    story.append(Paragraph(
        "Planograms are mandatory merchandising blueprints that dictate exact product placement on every "
        "shelf in the store. Compliance is measured at 95% accuracy or higher. Each planogram is generated "
        "by the Category Management team using JDA Space Planning software and distributed via the "
        "StoreConnect portal every Monday at 6:00 AM local time.",
        styles['BodyText2']
    ))
    story.append(Paragraph("3.2 Shelf Stocking Hierarchy", styles['SectionTitle']))
    story.append(Paragraph(
        "Products must be placed following the vertical blocking strategy: brand blocks run top-to-bottom, "
        "with premium/national brands at eye level (shelf positions 3-4 counting from bottom). Private "
        "label products occupy positions 1-2 (lower shelves) and position 5+ (top shelf). Children's "
        "products must always be placed at child eye level (shelves 1-2, 36-48 inches from floor).",
        styles['BodyText2']
    ))
    story.append(Paragraph("3.3 Facing Requirements by Category", styles['SectionTitle']))
    facing_data = [
        ["Category", "Min Facings", "Max Facings", "Shelf Position", "Special Notes"],
        ["Carbonated Beverages", "3", "8", "2-4", "Cold vault: label forward"],
        ["Snack Foods", "2", "6", "3-5", "Clip strips for new items"],
        ["Breakfast Cereals", "2", "5", "2-5", "Kids brands at shelf 2"],
        ["Laundry Detergent", "2", "4", "1-3", "Heavy items on bottom"],
        ["Baby Products", "2", "4", "2-3", "Security tags required"],
        ["Oral Care", "1", "3", "3-4", "Brand blocking vertical"],
        ["Coffee & Tea", "2", "5", "3-4", "Flavor blocking horizontal"],
        ["Canned Vegetables", "2", "4", "1-4", "Label out, pyramid stack"],
    ]
    t = Table(facing_data, colWidths=[1.4 * inch, 0.8 * inch, 0.8 * inch, 0.9 * inch, 2.3 * inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), BRAND_BLUE),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, MEDIUM_GRAY),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, LIGHT_GRAY]),
    ]))
    story.append(t)
    story.append(Spacer(1, 0.2 * inch))
    story.append(Paragraph("3.4 Out-of-Stock Protocol", styles['SectionTitle']))
    story.append(Paragraph(
        "When a product is out of stock, the following protocol must be followed in order: "
        "(1) Check backroom inventory within 15 minutes. (2) If unavailable, pull forward adjacent "
        "facings to fill the gap — never leave an empty shelf space visible to customers. "
        "(3) If the gap exceeds 2 facings wide, use approved shelf filler cards (blue for temporary, "
        "red for discontinued). (4) Log the out-of-stock in the StoreConnect app immediately. "
        "(5) For items out of stock more than 48 hours, request emergency replenishment from DC.",
        styles['BodyText2']
    ))
    story.append(Paragraph("3.5 Price Tag Placement", styles['SectionTitle']))
    story.append(Paragraph(
        "Electronic shelf labels (ESLs) must be centered below the leftmost facing of each product. "
        "The tag rail must be clean and free of old adhesive residue. When multiple sizes of the same "
        "product are adjacent, size callouts must be visible on the ESL. Promotional price tags use "
        "yellow background with red text. Clearance items use orange tags. All prices must match the "
        "POS system within a 0% tolerance — any discrepancy requires immediate correction.",
        styles['BodyText2']
    ))
    story.append(PageBreak())


def build_chapter4(story, styles):
    story.append(Paragraph("4. End-Cap & Promotional Display Setup", styles['ChapterTitle']))
    story.append(Paragraph("4.1 End-Cap Classification", styles['SectionTitle']))
    story.append(Paragraph(
        "End-caps are classified into four tiers based on traffic and visibility: Tier 1 (front-of-store, "
        "main aisle intersections) — reserved for national brand promotions and highest-revenue items. "
        "Tier 2 (mid-store aisle ends) — used for cross-merchandising and seasonal tie-ins. "
        "Tier 3 (back-of-store) — allocated to bulk deals and warehouse-style stacking. "
        "Tier 4 (side panels/wings) — impulse and add-on items only.",
        styles['BodyText2']
    ))
    story.append(Paragraph("4.2 Display Build Specifications", styles['SectionTitle']))
    specs = [
        "Maximum height: 5 feet from floor to top of product for free-standing displays.",
        "Base pallet displays must use approved riser pallets (Part #FM-RP-200) only.",
        "Cross-merchandising displays require approval from both category managers involved.",
        "All displays must include a header sign (minimum 11\" x 14\") with promotional pricing.",
        "QR codes linking to digital coupons must be placed at 48-54 inches from floor level.",
        "Power wing displays: maximum weight 15 lbs per wing, secured with anti-sway clips.",
        "Dump bins must not be filled above the rim; maintain 2-inch clearance from top edge.",
        "All promotional displays have a mandatory tear-down date printed on the setup instruction sheet.",
    ]
    for s in specs:
        story.append(Paragraph(f"• {s}", styles['BodyText2']))
    story.append(Paragraph("4.3 Promotional Calendar Integration", styles['SectionTitle']))
    promo_data = [
        ["Week", "Theme", "Primary Category", "Display Type", "Setup Day"],
        ["W1-W2", "New Year Wellness", "Health & Vitamins", "End-cap Tier 1", "Monday"],
        ["W3-W4", "Super Bowl Season", "Snacks & Beverages", "Pallet + End-cap", "Saturday"],
        ["W5-W8", "Valentine's Day", "Confectionery", "Floor stand", "Monday"],
        ["W9-W12", "Spring Cleaning", "Household Cleaners", "End-cap Tier 2", "Monday"],
        ["W13-W16", "Easter/Passover", "Seasonal Foods", "Themed island", "Saturday"],
        ["W17-W20", "Grilling Season", "Meat & Condiments", "Cross-merch display", "Monday"],
    ]
    t = Table(promo_data, colWidths=[0.7 * inch, 1.5 * inch, 1.5 * inch, 1.4 * inch, 1.1 * inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), BRAND_BLUE),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, MEDIUM_GRAY),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, LIGHT_GRAY]),
    ]))
    story.append(t)
    story.append(Spacer(1, 0.2 * inch))
    story.append(Paragraph("4.4 Vendor-Supplied Display Rules", styles['SectionTitle']))
    story.append(Paragraph(
        "Vendor-supplied shippers and displays must be pre-approved by the Regional Merchandising "
        "Coordinator. Unapproved vendor materials must be stored in the backroom and reported via "
        "StoreConnect. Approved vendor displays must still conform to aisle width requirements and "
        "fire code clearances. Vendor representatives are permitted to set displays only during "
        "designated windows (Tuesday/Thursday, 6:00 AM - 10:00 AM) and must check in at the "
        "service desk with valid ID and current vendor badge.",
        styles['BodyText2']
    ))
    story.append(Paragraph("4.5 Cross-Merchandising Guidelines", styles['SectionTitle']))
    story.append(Paragraph(
        "Cross-merchandising places complementary products together to increase basket size. Approved "
        "cross-merchandising combinations must follow the Category Affinity Matrix published quarterly "
        "by the Category Management team. Examples of approved combinations:",
        styles['BodyText2']
    ))
    cross_merch_data = [
        ["Primary Product", "Cross-Merch Item", "Display Method", "Lift Target"],
        ["Pasta (dry)", "Pasta sauce, Parmesan cheese", "Clip strip + shelf blade", "+12% basket"],
        ["Ground beef", "Hamburger buns, condiments", "Adjacent cooler + clip strip", "+18% basket"],
        ["Chips & salsa", "Beer/soda multi-packs", "Pallet + wing display", "+22% basket"],
        ["Pancake mix", "Maple syrup, fresh berries", "Inline shelf adjacency", "+15% basket"],
        ["Baby diapers", "Baby wipes, rash cream", "Wing panel display", "+25% basket"],
        ["Coffee (ground)", "Coffee filters, creamer", "Shelf blade + cooler tie-in", "+10% basket"],
        ["Charcoal", "Lighter fluid, grilling tools", "Pallet + floor stack", "+30% basket"],
    ]
    t = Table(cross_merch_data, colWidths=[1.2 * inch, 1.8 * inch, 1.8 * inch, 1 * inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), BRAND_BLUE),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, MEDIUM_GRAY),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, LIGHT_GRAY]),
    ]))
    story.append(t)
    story.append(Spacer(1, 0.2 * inch))
    story.append(Paragraph("4.6 Display Performance Tracking", styles['SectionTitle']))
    story.append(Paragraph(
        "Every promotional display must have a performance tracking card (Form FM-DPT-01) attached "
        "to its base or rear panel. The card records: setup date, planned teardown date, weekly unit "
        "movement, and final ROI calculation. Department managers photograph displays at setup and "
        "teardown for the display performance database. Displays not meeting minimum performance "
        "thresholds (50% of projected units sold by midpoint) may be relocated or replaced early "
        "with Regional Coordinator approval. Top-performing displays (150%+ of projection) are "
        "documented as best practices and shared in the monthly merchandising newsletter.",
        styles['BodyText2']
    ))
    story.append(Paragraph("4.7 Impulse Merchandise Zones", styles['SectionTitle']))
    story.append(Paragraph(
        "Impulse zones are high-traffic areas designed to capture unplanned purchases. The primary "
        "impulse zone is the checkout queue area (last 12 feet before the register). Secondary zones "
        "include: aisle power wings, entrance vestibule displays, and restroom corridor shelving. "
        "Products in impulse zones must be: (a) priced under $5.99, (b) small enough to add to "
        "an existing cart without rearranging, (c) visually appealing with strong packaging design, "
        "and (d) high-margin (minimum 45% gross margin). Category rotation in checkout impulse "
        "zones follows a 4-week cycle: Week 1 - Confectionery, Week 2 - Salty snacks, "
        "Week 3 - Beverages (single-serve), Week 4 - Seasonal/novelty items.",
        styles['BodyText2']
    ))
    story.append(PageBreak())


def build_chapter5(story, styles):
    story.append(Paragraph("5. Beverage Aisle Standards", styles['ChapterTitle']))
    story.append(Paragraph("5.1 Cold Vault Management", styles['SectionTitle']))
    story.append(Paragraph(
        "The cold vault (refrigerated beverage section) must maintain a temperature range of 34-38°F "
        "(1-3°C). All products must be front-faced with labels visible. The cold vault is restocked "
        "using the FIFO (First In, First Out) rotation method. Maximum door opening time for restocking "
        "is 10 minutes per section to maintain temperature compliance. Condensation on doors must be "
        "addressed immediately — report to maintenance if anti-fog heaters malfunction.",
        styles['BodyText2']
    ))
    story.append(Paragraph("5.2 Carbonated Soft Drink (CSD) Placement", styles['SectionTitle']))
    story.append(Paragraph(
        "CSDs follow a brand-block vertical merchandising strategy. Coca-Cola products occupy the "
        "first 3 door sections (left to right when facing the vault). PepsiCo products occupy "
        "sections 4-6. Private label and regional brands fill sections 7-8. Energy drinks are "
        "positioned in sections 9-10 at eye level. Water and enhanced water products are placed in "
        "the final 2-3 sections. All 2-liter and multi-pack items are on the bottom shelf.",
        styles['BodyText2']
    ))
    story.append(Paragraph("5.3 Ambient Beverage Shelving", styles['SectionTitle']))
    story.append(Paragraph(
        "Ambient (room temperature) beverages are merchandised on standard gondola shelving adjacent "
        "to the cold vault. The flow moves from single-serve (left) to multi-pack (right). Large "
        "format packs (24-pack, 36-pack) are floor-stacked on the bottom shelf or on approved "
        "riser pallets in front of the gondola. Maximum stack height for floor displays: 3 cases "
        "for 12-packs, 2 cases for 24-packs.",
        styles['BodyText2']
    ))
    story.append(Paragraph("5.4 Alcoholic Beverage Compliance", styles['SectionTitle']))
    story.append(Paragraph(
        "Where state/local laws permit alcohol sales: all alcoholic beverages must be in a clearly "
        "delineated section with appropriate signage (\"You must be 21 to purchase alcohol\"). "
        "Beer and wine coolers are in the cold vault's designated alcohol section. Spirits (where "
        "permitted) are in a locked cabinet or behind-counter display. No alcoholic beverages may "
        "be cross-merchandised with non-alcohol products. Age verification signage must be visible "
        "from 10 feet away. Security cameras must cover the entire alcohol section.",
        styles['BodyText2']
    ))
    story.append(Paragraph("5.5 Beverage Cooler Cleaning Schedule", styles['SectionTitle']))
    cleaning_data = [
        ["Task", "Frequency", "Responsible", "Duration"],
        ["Wipe door glass (interior/exterior)", "Daily", "Beverage Associate", "15 min"],
        ["Clean shelf rails and price channels", "Weekly", "Beverage Associate", "45 min"],
        ["Deep clean condenser coils", "Monthly", "Maintenance", "2 hours"],
        ["Temperature calibration check", "Weekly", "Dept. Manager", "10 min"],
        ["Replace LED lighting strips", "As needed", "Maintenance", "30 min"],
        ["Full cooler reset and defrost", "Quarterly", "Maintenance + Vendor", "4 hours"],
    ]
    t = Table(cleaning_data, colWidths=[2.5 * inch, 1 * inch, 1.5 * inch, 1 * inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), BRAND_BLUE),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 0.5, MEDIUM_GRAY),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, LIGHT_GRAY]),
    ]))
    story.append(t)
    story.append(PageBreak())


def build_chapter6(story, styles):
    story.append(Paragraph("6. Fresh Produce Display Requirements", styles['ChapterTitle']))
    story.append(Paragraph("6.1 Quality Standards", styles['SectionTitle']))
    story.append(Paragraph(
        "All produce on display must meet FreshMart Grade A standards: no visible bruising, wilting, "
        "or discoloration. Culling rounds must be performed every 2 hours during operating hours. "
        "Culled items below Grade B are discarded; Grade B items may be transferred to the prepared "
        "foods department for same-day use with department manager approval. Produce shrink target "
        "is below 4.5% of department sales.",
        styles['BodyText2']
    ))
    story.append(Paragraph("6.2 Display Temperature Zones", styles['SectionTitle']))
    temp_data = [
        ["Product Category", "Display Temp", "Humidity", "Max Display Time", "Misting"],
        ["Leafy Greens", "34-38°F", "90-95%", "24 hours", "Yes - every 30 min"],
        ["Root Vegetables", "45-50°F", "85-90%", "72 hours", "No"],
        ["Tropical Fruits", "55-60°F", "85-90%", "48 hours", "No"],
        ["Berries", "32-36°F", "90-95%", "24 hours", "No (damages fruit)"],
        ["Stone Fruits", "38-42°F", "85-90%", "48 hours", "No"],
        ["Citrus", "45-48°F", "85-90%", "96 hours", "No"],
        ["Herbs (fresh cut)", "34-38°F", "90-95%", "12 hours", "Yes - every 20 min"],
    ]
    t = Table(temp_data, colWidths=[1.3 * inch, 1 * inch, 0.8 * inch, 1.2 * inch, 1.7 * inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HexColor("#2E7D32")),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, MEDIUM_GRAY),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, LIGHT_GRAY]),
    ]))
    story.append(t)
    story.append(Spacer(1, 0.2 * inch))
    story.append(Paragraph("6.3 Wet Rack & Table Arrangement", styles['SectionTitle']))
    story.append(Paragraph(
        "Wet racks (misted display cases) are reserved for leafy greens, herbs, and green onions. "
        "Products on wet racks must be arranged using the waterfall technique — product cascades "
        "forward and downward, creating visual abundance. Tables use the basket display method with "
        "products mounded to 150% of container height at center, sloping to edges. Color blocking "
        "is mandatory: arrange by color spectrum (red > orange > yellow > green > purple) to create "
        "visual impact. Every display table must have a chalkboard-style sign with product name, "
        "origin, and price per pound/each.",
        styles['BodyText2']
    ))
    story.append(Paragraph("6.4 Organic & Specialty Produce", styles['SectionTitle']))
    story.append(Paragraph(
        "Organic produce must be physically separated from conventional products by a minimum of "
        "12 inches or by a clearly labeled divider. Organic items use green price tags; conventional "
        "use white. Local farm partnerships (within 100-mile radius) receive dedicated endcap space "
        "with farm story cards including farmer photo, farm name, distance from store, and farming "
        "practices. Local items are restocked same-day from farm deliveries where possible.",
        styles['BodyText2']
    ))
    story.append(PageBreak())


def build_chapter7(story, styles):
    story.append(Paragraph("7. Frozen Foods Merchandising", styles['ChapterTitle']))
    story.append(Paragraph("7.1 Freezer Case Management", styles['SectionTitle']))
    story.append(Paragraph(
        "All freezer cases must maintain a temperature of -10°F to 0°F (-23°C to -18°C). The load "
        "line (maximum fill level) on upright freezer doors must never be exceeded — product stacked "
        "above the load line blocks air circulation and causes temperature spikes. Open coffin-style "
        "freezers must not be filled above 2 inches below the rim. Temperature logs are recorded "
        "automatically via IoT sensors every 15 minutes and reviewed by department managers daily.",
        styles['BodyText2']
    ))
    story.append(Paragraph("7.2 Product Arrangement Strategy", styles['SectionTitle']))
    story.append(Paragraph(
        "Frozen food follows a meal-solution adjacency model: frozen entrees are adjacent to frozen "
        "vegetables, which are adjacent to frozen potatoes/sides. Ice cream and frozen desserts "
        "occupy a separate aisle section from meal items. Frozen breakfast items (waffles, breakfast "
        "sandwiches) are grouped together near the frozen juice section. Private label frozen items "
        "are placed at eye level (shelf position 3-4) per corporate strategy to drive margin.",
        styles['BodyText2']
    ))
    story.append(Paragraph("7.3 Door Merchandising Standards", styles['SectionTitle']))
    door_rules = [
        "Each freezer door must have a clear, unobstructed view of products — no condensation buildup.",
        "Door gaskets are inspected weekly; damaged gaskets are replaced within 24 hours.",
        "Suction-cup signage on freezer doors is prohibited — use approved magnetic sign holders only.",
        "Maximum 2 promotional clings per door, positioned in upper-left corner, not exceeding 20% of glass area.",
        "Night covers must be deployed 30 minutes after store closing to conserve energy.",
        "LED case lighting must illuminate all shelves evenly — no dark spots permitted.",
    ]
    for rule in door_rules:
        story.append(Paragraph(f"• {rule}", styles['BodyText2']))
    story.append(Paragraph("7.4 Frozen Food Rotation", styles['SectionTitle']))
    story.append(Paragraph(
        "FIFO rotation is critical in frozen foods. New stock is placed behind existing stock. "
        "Products within 30 days of expiration are moved to a clearly marked 'Reduced for Quick Sale' "
        "section at the end of the frozen aisle with a minimum 30% discount. Items within 7 days of "
        "expiration are pulled and donated to the FreshMart community food bank program if quality "
        "standards are met. No expired product may remain on the sales floor under any circumstances.",
        styles['BodyText2']
    ))
    story.append(Paragraph("7.5 Ice Cream & Frozen Novelty Standards", styles['SectionTitle']))
    story.append(Paragraph(
        "Ice cream requires a dedicated freezer section maintained at -15°F to -10°F (colder than "
        "standard frozen foods) to prevent texture degradation. Premium ice cream brands (pints) "
        "occupy the eye-level shelf in upright freezers with clear door visibility. Multi-packs and "
        "economy sizes are on lower shelves. Novelty items (ice cream bars, sandwiches, cones) are "
        "grouped by brand and merchandised in coffin-style open freezers near the aisle entrance "
        "for impulse visibility. Seasonal flavors receive temporary shelf expansion (+2 facings) "
        "during peak summer months (June-August). All ice cream products must be checked for "
        "freezer burn weekly; damaged items are marked down 50% or pulled if quality is unacceptable.",
        styles['BodyText2']
    ))
    story.append(Paragraph("7.6 Frozen Meal Solutions Center", styles['SectionTitle']))
    story.append(Paragraph(
        "Each store designates a 'Frozen Meal Solutions' section featuring complete meal bundles. "
        "This section is positioned at the front of the frozen aisle for maximum visibility. "
        "Displays include recipe cards (printed on waterproof stock) showing how to combine 2-3 "
        "frozen items into a complete meal. Example bundles: 'Italian Night' (frozen garlic bread + "
        "frozen lasagna + frozen vegetables), 'Taco Tuesday' (frozen taco shells + frozen seasoned "
        "beef + frozen peppers/onions). Bundles are priced 10-15% below individual item sum. "
        "Solution center inventory is reviewed weekly and refreshed monthly with new recipe themes. "
        "Digital screens above the solution center display 30-second cooking tutorials on loop.",
        styles['BodyText2']
    ))
    story.append(PageBreak())


def build_chapter8(story, styles):
    story.append(Paragraph("8. Safety & Compliance Protocols", styles['ChapterTitle']))
    story.append(Paragraph(
        "⚠ CRITICAL: All safety protocols in this chapter are mandatory. Non-compliance may result "
        "in disciplinary action up to and including termination.",
        styles['Warning']
    ))
    story.append(Paragraph("8.1 Display Stability Requirements", styles['SectionTitle']))
    story.append(Paragraph(
        "All free-standing displays must pass the 'push test' — a display must withstand 25 lbs of "
        "horizontal force at its highest point without tipping. Stack displays must be pyramidal "
        "(wider base, narrower top). Maximum height for any customer-accessible display is 6 feet. "
        "Displays above 6 feet are permitted only in non-customer areas (above the top shelf of "
        "perimeter walls) and must be secured with safety strapping.",
        styles['BodyText2']
    ))
    story.append(Paragraph("8.2 Fire Safety Compliance", styles['SectionTitle']))
    fire_data = [
        ["Requirement", "Standard", "Inspection Frequency"],
        ["Sprinkler head clearance", "18 inches minimum below", "Daily visual check"],
        ["Exit path clearance", "6 feet unobstructed width", "Every shift change"],
        ["Fire extinguisher access", "36 inches clearance around", "Weekly inspection"],
        ["Electrical panel access", "3 feet clearance in front", "Daily visual check"],
        ["Flammable item storage", "Below 4 feet height, away from heat", "Weekly audit"],
        ["Emergency lighting", "Functional backup battery", "Monthly test"],
    ]
    t = Table(fire_data, colWidths=[2.2 * inch, 2.2 * inch, 1.8 * inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HexColor("#CC0000")),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 0.5, MEDIUM_GRAY),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, LIGHT_GRAY]),
    ]))
    story.append(t)
    story.append(Spacer(1, 0.2 * inch))
    story.append(Paragraph("8.3 Hazardous Materials Handling", styles['SectionTitle']))
    story.append(Paragraph(
        "Household chemicals, automotive fluids, and pesticides must be stored on bottom shelves only "
        "(gravity containment principle). These items require secondary containment trays on shelving "
        "units. Leaking containers must be isolated immediately using spill kit (located at end of "
        "each chemical aisle). SDS (Safety Data Sheets) must be accessible within 30 seconds — stored "
        "in the red binder at the department manager's station and digitally on StoreConnect.",
        styles['BodyText2']
    ))
    story.append(Paragraph("8.4 Ergonomic Stacking Limits", styles['SectionTitle']))
    story.append(Paragraph(
        "No single associate should lift more than 50 lbs without assistance or mechanical aid. "
        "Products over 25 lbs must be stocked on shelves below waist height (below 36 inches). "
        "Case stacking in backroom staging areas: maximum 5 cases high for items under 20 lbs, "
        "3 cases high for items 20-40 lbs, 1 case high for items over 40 lbs. Team lifts required "
        "for any item over 75 lbs.",
        styles['BodyText2']
    ))
    story.append(Paragraph("8.5 Slip and Fall Prevention", styles['SectionTitle']))
    story.append(Paragraph(
        "Wet floor signs must be deployed within 30 seconds of any spill. Spills must be cleaned "
        "within 5 minutes. The produce department must have a dedicated floor mat at the misting "
        "station. All associates must wear slip-resistant footwear meeting ASTM F2913 standard. "
        "Weekly floor inspection reports are filed by the safety coordinator every Friday by 5 PM.",
        styles['BodyText2']
    ))
    story.append(Paragraph("8.6 Child Safety in Display Areas", styles['SectionTitle']))
    story.append(Paragraph(
        "Displays accessible to children must meet enhanced safety standards. No display in a "
        "child-accessible area (below 48 inches) may contain: glass containers, sharp-edged packaging, "
        "small parts that pose choking hazards, or heavy items that could cause injury if pulled down. "
        "Candy and toy displays at checkout must be secured so individual items cannot be pulled "
        "causing a cascade. Coin-operated machines and vending displays near the entrance must be "
        "bolted to the floor with anti-tip brackets. Shopping cart corrals must have child safety "
        "signage reminding parents to use cart seat belts.",
        styles['BodyText2']
    ))
    story.append(Paragraph("8.7 Recall Product Removal Procedure", styles['SectionTitle']))
    story.append(Paragraph(
        "When a product recall notification is received via StoreConnect alert (Priority 1 — Red Banner): "
        "(1) Immediately pull all affected SKUs from sales floor and backroom — target completion within "
        "60 minutes of notification. (2) Segregate recalled product in designated quarantine area "
        "(backroom shelf labeled 'RECALL - DO NOT SELL' with red tape). (3) Scan each unit's barcode "
        "into the recall tracking module for inventory reconciliation. (4) Replace shelf space with "
        "adjacent product facings — never leave empty space that could alert customers to an issue. "
        "(5) Store Manager must confirm 100% removal in StoreConnect within 2 hours. (6) Recalled "
        "product is held until vendor pickup or destruction instructions are received from Corporate "
        "Quality Assurance. Under no circumstances may recalled product be donated, discounted, or "
        "returned to the sales floor.",
        styles['BodyText2']
    ))
    story.append(Paragraph("8.8 Electrical Safety for Display Equipment", styles['SectionTitle']))
    story.append(Paragraph(
        "All powered displays (rotating platforms, LED-lit shelving, digital screens, refrigerated "
        "sampling stations) must be connected to GFCI-protected outlets. Extension cords are prohibited "
        "on the sales floor — all powered displays must reach a dedicated outlet within the cord length "
        "provided by the manufacturer. Cord management channels (floor-mounted, ADA-compliant) must "
        "be used when cords cross pedestrian pathways. Monthly electrical safety inspections cover: "
        "frayed cords, overloaded outlets, missing ground prongs, and overheating transformers. Any "
        "display showing signs of electrical fault (burning smell, sparking, excessive heat) must be "
        "immediately unplugged and reported as a Priority 1 maintenance request.",
        styles['BodyText2']
    ))
    story.append(PageBreak())


def build_chapter9(story, styles):
    story.append(Paragraph("9. Seasonal & Holiday Displays", styles['ChapterTitle']))
    story.append(Paragraph("9.1 Seasonal Transition Timeline", styles['SectionTitle']))
    story.append(Paragraph(
        "Seasonal transitions follow a strict calendar. Holiday displays are set 4-6 weeks before "
        "the event and torn down within 24 hours after. Post-holiday clearance occupies dedicated "
        "Zone F space. The transition crew (minimum 3 associates per shift) executes the changeover "
        "during overnight hours (10 PM - 6 AM) to minimize customer disruption.",
        styles['BodyText2']
    ))
    story.append(Paragraph("9.2 Holiday Display Specifications", styles['SectionTitle']))
    holiday_data = [
        ["Holiday", "Setup Window", "Teardown", "Display Budget", "Theme Colors"],
        ["Valentine's Day", "Jan 15 - Feb 14", "Feb 15", "$2,500", "Red, Pink, White"],
        ["Easter", "Mar 1 - Easter", "Day after", "$3,000", "Pastel, Yellow, Green"],
        ["4th of July", "Jun 15 - Jul 4", "Jul 5", "$2,000", "Red, White, Blue"],
        ["Halloween", "Sep 15 - Oct 31", "Nov 1", "$4,000", "Orange, Black, Purple"],
        ["Thanksgiving", "Nov 1 - Thanksgiving", "Day after", "$2,500", "Orange, Brown, Gold"],
        ["Christmas/Holiday", "Nov 1 - Dec 25", "Dec 26", "$8,000", "Red, Green, Gold, Silver"],
    ]
    t = Table(holiday_data, colWidths=[1.2 * inch, 1.3 * inch, 0.8 * inch, 1 * inch, 1.7 * inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), BRAND_ORANGE),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, MEDIUM_GRAY),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, LIGHT_GRAY]),
    ]))
    story.append(t)
    story.append(Spacer(1, 0.2 * inch))
    story.append(Paragraph("9.3 Back-to-School Merchandising", styles['SectionTitle']))
    story.append(Paragraph(
        "Back-to-School (BTS) displays launch July 15 and run through September 15. Primary "
        "categories include: school supplies, lunch items, snack packs, breakfast on-the-go, "
        "and household cleaning supplies. BTS displays use a 'solutions' merchandising approach — "
        "grouping items by use case (e.g., 'Lunch Box Essentials' bundles juice boxes, granola bars, "
        "fruit cups, and sandwich bags together regardless of home aisle). Cross-department "
        "collaboration between grocery, GM, and HBC is required.",
        styles['BodyText2']
    ))
    story.append(Paragraph("9.4 Weather-Responsive Merchandising", styles['SectionTitle']))
    story.append(Paragraph(
        "Stores must implement weather-responsive display changes based on the weekly forecast "
        "provided by the Weather Integration Module in StoreConnect. When temperatures exceed 90°F: "
        "increase cold beverage display space by 30%, add secondary ice cream freezer to front-of-store. "
        "When temperatures drop below 32°F: feature hot beverages, soups, and comfort foods at "
        "front-of-store end-caps. Rainy week forecasts: move umbrella/rain gear displays to the "
        "entrance vestibule and increase hot beverage cross-merchandising.",
        styles['BodyText2']
    ))
    story.append(Paragraph("9.5 Post-Holiday Markdown Protocol", styles['SectionTitle']))
    story.append(Paragraph(
        "Post-holiday markdown follows a strict descending price schedule to clear seasonal inventory: "
        "Day 1 after holiday: 25% off all seasonal items. Day 3: 50% off remaining seasonal inventory. "
        "Day 7: 75% off — consolidate to single clearance end-cap. Day 14: remaining items are donated "
        "or destroyed (food items donated to food bank if within date; non-food items donated to "
        "community partners). Seasonal candy follows accelerated markdown: 50% on Day 1 to prevent "
        "inventory aging. All post-holiday clearance must be contained within Zone F — it must not "
        "encroach on incoming seasonal setup for the next holiday. Christmas clearance and Valentine's "
        "Day setup frequently overlap; dedicated teams handle each simultaneously.",
        styles['BodyText2']
    ))
    story.append(Paragraph("9.6 Cultural & Religious Holiday Sensitivity", styles['SectionTitle']))
    story.append(Paragraph(
        "FreshMart serves diverse communities. Holiday merchandising must be culturally inclusive: "
        "Stores in areas with significant Jewish populations (identified by demographic overlay in "
        "StoreConnect) must include Hanukkah/Passover displays of equivalent prominence to Christmas/"
        "Easter. Diwali, Lunar New Year, Eid, and other cultural celebrations receive dedicated "
        "end-cap space in stores where community demand exists (threshold: 15%+ of trade area "
        "population). All seasonal signage must use inclusive language ('Holiday Season' vs. "
        "'Christmas Season' in diverse markets). Religious symbols on signage require approval "
        "from the Diversity & Inclusion team. Stores should partner with local cultural organizations "
        "for authentic product selection and display guidance.",
        styles['BodyText2']
    ))
    story.append(Paragraph("9.7 Summer Outdoor Living Displays", styles['SectionTitle']))
    story.append(Paragraph(
        "Stores with outdoor garden centers or vestibule space deploy 'Outdoor Living' seasonal "
        "displays from April 15 through September 15. Products include: sunscreen, insect repellent, "
        "disposable tableware, charcoal, coolers, and outdoor games. These displays use weather-resistant "
        "fixtures (powder-coated steel, UV-resistant signage) and must be secured against wind with "
        "sandbag bases or ground stakes. Inventory checks occur twice daily (AM opening and PM mid-shift) "
        "due to higher theft risk in outdoor areas. Products displayed outdoors must not be temperature-"
        "sensitive (no chocolate, no aerosols above 120°F). End-of-season teardown includes fixture "
        "cleaning, inventory counting, and storage in designated backroom location for following year.",
        styles['BodyText2']
    ))
    story.append(PageBreak())


def build_chapter10(story, styles):
    story.append(Paragraph("10. Digital Signage & Price Tag Standards", styles['ChapterTitle']))
    story.append(Paragraph("10.1 Electronic Shelf Label (ESL) System", styles['SectionTitle']))
    story.append(Paragraph(
        "FreshMart uses the PriSync 5000 ESL system across all store formats. Labels update "
        "automatically via Wi-Fi at 3:00 AM daily and on-demand during promotional price changes. "
        "Associates must verify ESL accuracy during morning zone walks (6:00 AM - 7:00 AM). "
        "Any label showing 'ERROR' or 'NO SIGNAL' must be reported to IT within 1 hour. Battery "
        "life is approximately 5 years; labels displaying low-battery icon are replaced monthly "
        "by the ESL maintenance team.",
        styles['BodyText2']
    ))
    story.append(Paragraph("10.2 Digital Endcap Screens", styles['SectionTitle']))
    story.append(Paragraph(
        "Each Tier 1 and Tier 2 end-cap is equipped with a 32-inch digital display screen. Content "
        "is managed centrally by the Marketing team via the ContentSync CMS. Store-level overrides "
        "require Regional Director approval. Screens cycle through: promotional video (15 sec), "
        "price callout (10 sec), recipe suggestion (10 sec), and loyalty program reminder (5 sec). "
        "Screen brightness adjusts automatically based on ambient light sensors. Screens in the "
        "alcohol section must display responsible drinking messaging for minimum 20% of cycle time.",
        styles['BodyText2']
    ))
    story.append(Paragraph("10.3 Printed Sign Standards", styles['SectionTitle']))
    sign_data = [
        ["Sign Type", "Size", "Color Scheme", "Placement", "Authority to Create"],
        ["Regular Price", "2\" x 3\"", "Black on white", "Shelf edge channel", "Auto-generated"],
        ["Sale Price", "3\" x 5\"", "Red on yellow", "Shelf edge channel", "Category Manager"],
        ["BOGO Offer", "5\" x 7\"", "White on red", "Shelf talker", "Promo Team"],
        ["Clearance", "3\" x 5\"", "Black on orange", "Shelf edge + topper", "Store Manager"],
        ["New Item", "2\" x 4\"", "White on green", "Shelf blade", "Auto-generated"],
        ["Local/Organic", "3\" x 4\"", "Green on cream", "Basket/table sign", "Produce Manager"],
        ["Endcap Header", "11\" x 14\"", "Brand-specific", "Header holder", "Marketing"],
    ]
    t = Table(sign_data, colWidths=[1 * inch, 0.7 * inch, 1.1 * inch, 1.3 * inch, 1.5 * inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), BRAND_BLUE),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, MEDIUM_GRAY),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, LIGHT_GRAY]),
    ]))
    story.append(t)
    story.append(Spacer(1, 0.2 * inch))
    story.append(Paragraph("10.4 QR Code Integration", styles['SectionTitle']))
    story.append(Paragraph(
        "All promotional displays must include at least one QR code linking to the FreshMart app "
        "for digital coupon clipping. QR codes must be printed at minimum 1.5\" x 1.5\" size for "
        "reliable scanning. Placement height: 48-54 inches from floor (average smartphone scanning "
        "height). QR codes must be tested weekly — non-functional codes are replaced within 4 hours. "
        "Analytics from QR scan rates are reviewed in weekly merchandising meetings.",
        styles['BodyText2']
    ))
    story.append(Paragraph("10.5 In-Store Audio & Announcement Standards", styles['SectionTitle']))
    story.append(Paragraph(
        "The in-store audio system supports merchandising through scheduled promotional announcements. "
        "Announcements are limited to 4 per hour, maximum 30 seconds each. Content is pre-recorded "
        "by the Marketing team and loaded into the AudioSync system weekly. Store-level live "
        "announcements are restricted to: safety alerts, department assistance calls, and store "
        "closing warnings. Background music volume must not exceed 65 dB at any point in the store. "
        "During promotional events (sampling, demos), localized speakers may be used at the event "
        "station with maximum 5-foot sound radius at 70 dB. Speakers must not face competing "
        "brand sections.",
        styles['BodyText2']
    ))
    story.append(Paragraph("10.6 Loyalty Program Display Integration", styles['SectionTitle']))
    story.append(Paragraph(
        "FreshMart Rewards program signage must be visible from every aisle. Minimum placement: "
        "one loyalty program shelf wobbler per 8-foot gondola section highlighting member-exclusive "
        "pricing. End-cap displays featuring loyalty-exclusive prices must include the FreshMart "
        "Rewards logo (minimum 3 inches wide) and the tagline 'Members Save More.' Digital screens "
        "dedicate 20% of rotation time to loyalty messaging. Checkout lane displays include "
        "loyalty signup cards (replenished daily). Stores are measured on weekly new loyalty "
        "signups — target: 50 new members per store per week. Displays promoting the mobile app "
        "download use a dedicated QR code (separate from product-level QR codes) linking directly "
        "to app store download page.",
        styles['BodyText2']
    ))
    story.append(Paragraph("10.7 Accessibility Compliance for Signage", styles['SectionTitle']))
    story.append(Paragraph(
        "All permanent signage must comply with ADA accessibility requirements: minimum 70% contrast "
        "ratio between text and background, minimum font size of 24pt for hanging signs visible from "
        "more than 8 feet, sans-serif fonts only (approved: Helvetica, Arial, Gotham). Braille "
        "equivalents are required on all permanent department identification signs, restroom signs, "
        "and emergency exit signs. Price tags must use minimum 12pt font. Promotional signs at "
        "child height (below 48 inches) must not contain language or imagery inappropriate for "
        "minors. Digital screens must include captioning for any video content with spoken audio. "
        "Flashing content is prohibited (seizure risk compliance per WCAG 2.1 guidelines).",
        styles['BodyText2']
    ))
    story.append(PageBreak())


def build_chapter11(story, styles):
    story.append(Paragraph("11. Audit Checklists & Scoring", styles['ChapterTitle']))
    story.append(Paragraph("11.1 Weekly Self-Audit Process", styles['SectionTitle']))
    story.append(Paragraph(
        "Every store must complete a Weekly Merchandising Self-Audit (WMSA) by Friday at 5:00 PM. "
        "The audit is performed by the Assistant Store Manager using the StoreConnect mobile app. "
        "Photos are required for each section. Results are automatically submitted to the Regional "
        "Merchandising Coordinator. Stores scoring below 80% must submit a corrective action plan "
        "within 48 hours.",
        styles['BodyText2']
    ))
    story.append(Paragraph("11.2 Scoring Methodology", styles['SectionTitle']))
    scoring_data = [
        ["Category", "Weight", "Score 5 (Excellent)", "Score 3 (Acceptable)", "Score 1 (Fail)"],
        ["Planogram Compliance", "25%", ">95% accurate", "85-95% accurate", "<85% accurate"],
        ["Display Condition", "20%", "Perfect execution", "Minor issues", "Major deficiencies"],
        ["Price Accuracy", "20%", "100% accurate", "98-99% accurate", "<98% accurate"],
        ["Stock Levels", "15%", "<2% OOS visible", "2-5% OOS visible", ">5% OOS visible"],
        ["Cleanliness", "10%", "Spotless", "Minor debris", "Dirty/unkempt"],
        ["Safety Compliance", "10%", "Zero violations", "Minor issues noted", "Critical violation"],
    ]
    t = Table(scoring_data, colWidths=[1.3 * inch, 0.6 * inch, 1.3 * inch, 1.3 * inch, 1.3 * inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), BRAND_BLUE),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, MEDIUM_GRAY),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, LIGHT_GRAY]),
    ]))
    story.append(t)
    story.append(Spacer(1, 0.2 * inch))
    story.append(Paragraph("11.3 Monthly Regional Audit", styles['SectionTitle']))
    story.append(Paragraph(
        "Regional Merchandising Coordinators conduct unannounced monthly audits at each store. "
        "The audit covers all 6 scoring categories plus additional items: associate knowledge test "
        "(ask 3 random associates about current promotions), backroom organization, receiving dock "
        "staging area, and promotional calendar adherence. Monthly audits use a 200-point scale. "
        "Stores averaging below 150/200 for two consecutive months are placed on Performance "
        "Improvement Plan (PIP) with weekly regional oversight.",
        styles['BodyText2']
    ))
    story.append(Paragraph("11.4 Corrective Action Process", styles['SectionTitle']))
    story.append(Paragraph(
        "When an audit identifies non-compliance, the following escalation process applies: "
        "Level 1 (score 70-79%): Store manager submits written corrective plan within 48 hours; "
        "re-audit in 7 days. Level 2 (score 60-69%): District Manager is notified; store manager "
        "and team lead attend remediation training within 5 business days; re-audit in 14 days. "
        "Level 3 (score below 60%): VP of Operations is notified; store receives daily oversight "
        "visits from district team for 30 days; personnel review initiated.",
        styles['BodyText2']
    ))
    story.append(Paragraph("11.5 Best Practice Recognition", styles['SectionTitle']))
    story.append(Paragraph(
        "Stores scoring 95%+ on three consecutive monthly audits receive 'Gold Standard' recognition: "
        "plaque displayed in break room, team bonus of $500 split among merchandising staff, "
        "and photo feature in the monthly FreshMart internal newsletter. The top-scoring store "
        "in each region annually receives the 'Excellence in Execution' award presented at the "
        "National Store Managers Conference.",
        styles['BodyText2']
    ))
    story.append(PageBreak())


def build_chapter12(story, styles):
    story.append(Paragraph("12. Appendix: Quick Reference Cards", styles['ChapterTitle']))
    story.append(Paragraph("12.1 Daily Opening Checklist — Merchandising", styles['SectionTitle']))
    morning_tasks = [
        "6:00 AM — Walk all aisles; identify overnight stock-out gaps and fill from backroom.",
        "6:15 AM — Verify all ESL labels are active (no ERROR/blank screens).",
        "6:30 AM — Check all end-cap displays for stability and product availability.",
        "6:45 AM — Inspect produce wet racks; start misting system; cull Grade C items.",
        "7:00 AM — Verify promotional signage matches current ad circular (check StoreConnect).",
        "7:15 AM — Ensure checkout lane impulse racks are fully stocked (gum, mints, magazines).",
        "7:30 AM — Confirm all cooler/freezer temperatures within acceptable ranges.",
        "7:45 AM — Verify digital screens are cycling correctly at all end-cap positions.",
        "8:00 AM — Store opens; zone walk with department leads to brief on today's priorities.",
    ]
    for task in morning_tasks:
        story.append(Paragraph(f"□ {task}", styles['BodyText2']))
    story.append(Spacer(1, 0.2 * inch))
    story.append(Paragraph("12.2 Emergency Display Teardown Procedure", styles['SectionTitle']))
    story.append(Paragraph(
        "If a display becomes unstable, is damaged, or poses a safety hazard, execute the following "
        "emergency procedure immediately:",
        styles['BodyText2']
    ))
    emergency_steps = [
        "STOP — Prevent customers from approaching. Deploy caution cones within 10 feet radius.",
        "ASSESS — Determine if the display can be safely stabilized or must be fully dismantled.",
        "NOTIFY — Radio store manager and loss prevention immediately (Code Yellow).",
        "SECURE — If product is on the floor, remove trip hazards first. Document with photos.",
        "RESOLVE — Stabilize or remove display. Clean the area. File incident report in StoreConnect.",
        "FOLLOW-UP — Review root cause with department lead within 24 hours. Update risk register.",
    ]
    for i, step in enumerate(emergency_steps, 1):
        story.append(Paragraph(f"{i}. {step}", styles['BodyText2']))
    story.append(Spacer(1, 0.2 * inch))
    story.append(Paragraph("12.3 Key Contacts", styles['SectionTitle']))
    contacts_data = [
        ["Role", "Contact Method", "Response Time"],
        ["Store Manager (on-duty)", "Radio Channel 1", "Immediate"],
        ["Regional Merch Coordinator", "StoreConnect message", "4 hours"],
        ["Vendor Relations Hotline", "1-800-555-0142", "Same business day"],
        ["Maintenance Emergency", "Radio Channel 3", "30 minutes"],
        ["IT Help Desk (ESL/Digital)", "1-800-555-0199 or ext. 4411", "2 hours"],
        ["Safety Incident Hotline", "1-800-555-0177", "Immediate callback"],
        ["Loss Prevention", "Radio Channel 2", "Immediate"],
    ]
    t = Table(contacts_data, colWidths=[2 * inch, 2.5 * inch, 1.5 * inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), BRAND_BLUE),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 0.5, MEDIUM_GRAY),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, LIGHT_GRAY]),
    ]))
    story.append(t)
    story.append(Spacer(1, 0.3 * inch))
    story.append(Paragraph("12.4 Weekly Promotional Changeover Procedure", styles['SectionTitle']))
    story.append(Paragraph(
        "Promotional changeovers occur every Wednesday evening (after 9:00 PM) or Thursday morning "
        "(before 6:00 AM store opening). The changeover team (minimum 2 associates plus department "
        "lead) follows this sequence:",
        styles['BodyText2']
    ))
    changeover_steps = [
        "Print new week's promotional plan from StoreConnect (includes display photos, signing spec, product list).",
        "Remove all expired promotional signage from end-caps, shelf edges, and hanging positions.",
        "Verify all promotional product is received and staged in backroom — flag shortages immediately.",
        "Build new displays per photographic specifications — use display build sheet for dimensions.",
        "Install new promotional signage — verify prices match POS system before opening.",
        "Take 'after' photos of each completed display and upload to StoreConnect verification module.",
        "Walk the full store at 5:45 AM to verify no missed changeovers before customer entry.",
        "Report any discrepancies (missing product, wrong signage, damaged fixtures) by 7:00 AM.",
    ]
    for i, step in enumerate(changeover_steps, 1):
        story.append(Paragraph(f"{i}. {step}", styles['BodyText2']))
    story.append(Spacer(1, 0.2 * inch))
    story.append(Paragraph("12.5 Store Closing Merchandising Checklist", styles['SectionTitle']))
    closing_tasks = [
        "Pull forward all products on shelves visible from main aisles (zone A and B minimum).",
        "Remove any damaged or leaking product discovered during closing walk.",
        "Verify all refrigerated/frozen case doors are fully closed and sealed.",
        "Deploy night covers on all open-top coffin cases (frozen, dairy, deli).",
        "Power down non-essential digital signage (leave emergency and directional signs active).",
        "Secure all outdoor displays and bring weather-sensitive items inside vestibule.",
        "Set in-store audio to overnight mode (security announcements only).",
        "Arm anti-theft systems on high-value display cases (electronics, razors, baby formula).",
    ]
    for task in closing_tasks:
        story.append(Paragraph(f"□ {task}", styles['BodyText2']))
    story.append(Spacer(1, 0.3 * inch))
    story.append(Paragraph("12.6 Abbreviations & Glossary", styles['SectionTitle']))
    glossary = [
        ["Term", "Definition"],
        ["BOGO", "Buy One Get One (Free or discounted)"],
        ["CSD", "Carbonated Soft Drink"],
        ["DC", "Distribution Center"],
        ["ESL", "Electronic Shelf Label"],
        ["FIFO", "First In, First Out (stock rotation method)"],
        ["OOS", "Out Of Stock"],
        ["PIP", "Performance Improvement Plan"],
        ["PLU", "Price Look-Up (code for produce/bulk items)"],
        ["POG", "Planogram"],
        ["POS", "Point Of Sale (checkout system)"],
        ["SDS", "Safety Data Sheet"],
        ["SKU", "Stock Keeping Unit"],
        ["SOP", "Standard Operating Procedure"],
        ["WMSA", "Weekly Merchandising Self-Audit"],
    ]
    t = Table(glossary, colWidths=[1 * inch, 5 * inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), BRAND_BLUE),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 0.5, MEDIUM_GRAY),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, LIGHT_GRAY]),
    ]))
    story.append(t)
    story.append(Spacer(1, 0.3 * inch))
    story.append(Paragraph("12.7 Compliance Sign-Off Sheet", styles['SectionTitle']))
    story.append(Paragraph(
        "Each store must maintain a signed acknowledgment that all merchandising personnel have "
        "read and understood this manual. The following sign-off is required annually and upon "
        "any major revision (version change in first decimal place, e.g., 4.1 to 4.2):",
        styles['BodyText2']
    ))
    signoff_data = [
        ["Name (Print)", "Role/Title", "Signature", "Date"],
        ["_________________", "_________________", "_________________", "___/___/______"],
        ["_________________", "_________________", "_________________", "___/___/______"],
        ["_________________", "_________________", "_________________", "___/___/______"],
        ["_________________", "_________________", "_________________", "___/___/______"],
        ["_________________", "_________________", "_________________", "___/___/______"],
        ["_________________", "_________________", "_________________", "___/___/______"],
        ["_________________", "_________________", "_________________", "___/___/______"],
        ["_________________", "_________________", "_________________", "___/___/______"],
    ]
    t = Table(signoff_data, colWidths=[1.8 * inch, 1.5 * inch, 1.8 * inch, 1.2 * inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), BRAND_BLUE),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 0.5, MEDIUM_GRAY),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ('TOPPADDING', (0, 1), (-1, -1), 10),
    ]))
    story.append(t)
    story.append(Spacer(1, 0.3 * inch))
    story.append(Paragraph(
        "Store Manager Certification: I confirm that all merchandising personnel in this location "
        "have been trained on the contents of this manual and understand their responsibilities "
        "for compliance.",
        styles['BodyText2']
    ))
    story.append(Spacer(1, 0.3 * inch))
    story.append(Paragraph("Store Manager Signature: _________________________ Date: ___/___/______", styles['BodyText2']))
    story.append(Paragraph("Store Number: _________ District: _________ Region: _________", styles['BodyText2']))
    story.append(Spacer(1, 0.8 * inch))
    story.append(Paragraph(
        "— END OF DOCUMENT —<br/><br/>"
        "For questions regarding this manual, contact the Visual Merchandising & Store Standards "
        "department at merchandising@freshmart-global.com or ext. 2200.",
        styles['BodyText2']
    ))
    story.append(Spacer(1, 0.3 * inch))
    story.append(Paragraph(
        "© 2025 FreshMart Global Retail Corporation. All rights reserved.<br/>"
        "Unauthorized distribution of this document is strictly prohibited.",
        styles['Footer']
    ))


def add_page_number(canvas, doc):
    page_num = canvas.getPageNumber()
    if page_num > 1:
        canvas.saveState()
        canvas.setFont('Helvetica', 8)
        canvas.setFillColor(MEDIUM_GRAY)
        canvas.drawCentredString(4.25 * inch, 0.5 * inch, f"FreshMart Retail Display Manual v4.2 — Page {page_num}")
        canvas.restoreState()


def main():
    doc = SimpleDocTemplate(
        OUTPUT_PATH,
        pagesize=letter,
        rightMargin=0.75 * inch,
        leftMargin=0.75 * inch,
        topMargin=0.75 * inch,
        bottomMargin=0.75 * inch,
    )

    styles = get_styles()
    story = []

    build_cover_page(story, styles)
    build_toc(story, styles)
    build_chapter1(story, styles)
    build_chapter2(story, styles)
    build_chapter3(story, styles)
    build_chapter4(story, styles)
    build_chapter5(story, styles)
    build_chapter6(story, styles)
    build_chapter7(story, styles)
    build_chapter8(story, styles)
    build_chapter9(story, styles)
    build_chapter10(story, styles)
    build_chapter11(story, styles)
    build_chapter12(story, styles)

    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print(f"PDF generated successfully: {OUTPUT_PATH}")
    print(f"File size: {os.path.getsize(OUTPUT_PATH) / 1024:.1f} KB")


if __name__ == "__main__":
    main()
