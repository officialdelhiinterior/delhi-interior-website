import os, json

os.makedirs('scripts', exist_ok=True)

SERVICES_DATA = [
    {
        'slug': 'modular-kitchen-delhi',
        'title': 'Modular Kitchen in Delhi | Custom Design & Installation | Delhi Interior',
        'desc': 'Best modular kitchen designers in Delhi. Custom base cabinets, wall units, quartz counters & Hettich hardware. Free design consultation. Master craftsmanship. Call now.',
        'h1': 'Modular Kitchen Design in Delhi',
        'sub': 'Precision-engineered modular kitchens built for Indian cooking — heat, oil, and water resistant with German soft-close fittings.',
        'hero_img': '/assets/images/service-kitchen.webp',
        'alt': 'Modular kitchen design by Delhi Interior in Delhi',
        'overview_h2': 'Engineered for Indian Cooking. Crafted for Elegance.',
        'overview_p1': 'A kitchen in an Indian home isn\'t just a culinary space — it is the high-traffic engine of the household. From heavy stainless steel kadhais and deep frying to rigorous wet cleaning, a kitchen needs to withstand punishing everyday use. We build custom modular kitchens crafted from certified Marine-Grade BWP (Boiling Water Proof) plywood, anti-scratch acrylic and PU shutters, and stain-resistant quartz countertops.',
        'overview_p2': 'Whether you have a compact L-shaped layout, an expansive parallel layout, or desire a grand island kitchen with breakfast counter, our master craftsmen engineer every carcass and shutter down to the exact millimetre.',
        'checklist': [
            'Marine Grade BWP (Boiling Water Proof) Plywood Carcass',
            'German Soft-Close Tandem Drawers (Hettich / Ebco)',
            'Stain & Scratch Resistant Quartz or Granite Countertop',
            'Full Pantry Pullout Units & Tall Appliance Towers',
            'LeMans Blind Corner & Magic Corner Optimizers',
            'Custom Cutlery Trays, Thali Baskets & Spice Organizers',
            'Concealed Profile Under-Cabinet LED Lighting',
            'Dedicated Hob & Chimney Precision Cutouts',
            'Under-Mount Quartz Sink & Anti-Leak CPVC Fittings',
            'Anti-Bacterial PVC Edge Banding on All 4 Sides'
        ],
        'process_steps': [
            ('Consultation & Measurement', 'Detailed site visit in Delhi NCR, laser room scan, and architectural layout consultation.'),
            ('Architectural Working Drawings Design', 'Interactive 3D renders with color swatches, finish selection, and revision iterations.'),
            ('Factory Build & Handover', 'Factory precision cutting, edge-banding, on-site assembly, and zero-defect handover.')
        ],
        'gallery': [
            ('/assets/images/portfolio-kitchen.webp', 'L-Shaped Matte Acrylic Kitchen', 'Greater Kailash II'),
            ('/assets/images/hero-kitchen.webp', 'Island Kitchen with Breakfast Bar', 'Golf Links, New Delhi'),
            ('/assets/images/portfolio-kitchen-2.webp', 'Parallel Modular Kitchen', 'DLF Phase 5, Gurugram'),
            ('/assets/images/portfolio-dining.webp', 'Open Concept Kitchen & Dining', 'Vasant Vihar'),
            ('/assets/images/portfolio-fullhome.webp', 'Minimalist Handleless Kitchen', 'Defence Colony'),
            ('/assets/images/service-kitchen.webp', 'Classic Shaker Style Kitchen', 'Chanakyapuri')
        ],
        'pricing': [
            ('Economy', '₹1.5 Lakh – ₹2.8 Lakh', ['BWR Plywood Base', '1mm Branded Laminates', 'Standard Soft-Close Channels', 'Granite Countertop Prepped', 'Quality Audit & Handover']),
            ('Standard (Most Popular)', '₹2.8 Lakh – ₹4.8 Lakh', ['BWP Marine Grade Plywood', 'Anti-Scratch Acrylic Shutters', 'Hettich / Ebco Tandem Drawers', 'Quartz Countertop Included', 'Profile Lighting & Concealed Channels']),
            ('Luxury Editorial', '₹4.8 Lakh – ₹8.5 Lakh+', ['HDMR & BWP Hybrid Build', 'PU Lacquered / Fluted Glass Shutters', 'Blum Servo-Drive Motorized Lift', 'Imported Calacatta Quartz Slab', 'Comprehensive Quality Assurance'])
        ],
        'faqs': [
            ('How do you determine the scope for a custom modular kitchen in Delhi?', 'Our modular kitchen solutions are custom planned based on your exact layout, counter dimensions, and storage needs. Every design includes architectural layouts, genuine BWP 710 marine ply, premium quartz, and German soft-close fittings with an itemized BOQ commitment.'),
            ('Which plywood grade is best for Indian kitchens?', 'We strictly recommend BWP (Boiling Water Proof) 710-grade plywood for kitchen sink and base units because it withstands steam, water spills, and heavy load without delamination.'),
            ('How long does modular kitchen installation take?', 'Fabrication takes approximately 20–25 days in our facility. Once delivered on site, our in-house carpentry team installs the kitchen in 3 to 5 working days.'),
            ('Do you provide civil modifications, plumbing, and chimney ducting?', 'Yes. Delhi Interior is a full-service studio. We manage core-cutting for chimney exhaust, plumbing relocation, tile dado work, and electrical switch points under one turnkey contract.'),
            ('What hardware brands do you offer?', 'We work exclusively with certified international brands including Hettich, Ebco, Blum, and Hafele, all installed to authentic manufacturer specifications.')
        ],
        'related': [
            ('Wardrobe Design in Delhi', '/wardrobe-design-delhi/', 'Custom floor-to-ceiling wardrobes with soft-close sliding and hinged shutters.'),
            ('Wall Paneling & TV Units', '/wall-paneling-delhi/', 'Acoustic fluted slats, charcoal panels, and floating luxury media backdrops.'),
            ('Full Home Turnkey Interiors', '/full-home-interior-delhi/', 'Comprehensive 2BHK and 3BHK turnkey transformations delivered in 45-60 days.')
        ]
    },
    {
        'slug': 'wardrobe-design-delhi',
        'title': 'Wardrobe Design in Delhi | Custom Almirah & Closets | Delhi Interior',
        'desc': 'Custom wardrobe designers in Delhi. Floor-to-ceiling sliding & hinged wardrobes, walk-in closets, hydraulic storage. Master craftsmanship. Free design consultation.',
        'h1': 'Custom Wardrobe Design in Delhi',
        'sub': 'Floor-to-ceiling custom wardrobes, walk-in closets, and dressing consoles engineered for maximum storage and timeless aesthetics.',
        'hero_img': '/assets/images/service-wardrobe.webp',
        'alt': 'Custom wardrobe design by Delhi Interior in Delhi',
        'overview_h2': 'Built to the Millimetre. Tailored to Your Wardrobe.',
        'overview_p1': 'Off-the-shelf wardrobes leave wasteful gaps between the top of the cabinet and your ceiling where dust accumulates. At Delhi Interior, our bespoke wardrobes are built floor-to-ceiling, gaining up to 35% more functional storage space. From dedicated saree pullouts and tie racks to concealed biometric vanity lockers, every compartment is designed around your daily lifestyle.',
        'overview_p2': 'Choose between space-saving smooth top-hung sliding systems, classic shaker-style hinged doors, or high-fashion tinted glass walk-in closets with automatic sensor profile illumination.',
        'checklist': [
            'Full Floor-to-Ceiling Loft Maximization',
            'Heavy-Duty Top-Hung Sliding Systems (No Lower Dust Track)',
            'Hettich Sensys Soft-Close Hinges with 110° Opening',
            'Concealed Motion-Sensor LED Wardrobe Profile Lights',
            'Dedicated Saree Trays, Trouser Racks & Tie Organizers',
            'Velvet-Lined Jewellery Drawers with Dividers',
            'Concealed Digital / Biometric Safe Integration',
            'Anti-Warping Aluminum Stiffener Bars for Tall Shutters',
            'Tinted Bronze Glass, Fluted Glass & Mirror Shutters',
            'Hydraulic Pull-Down Wardrobe Lift Rails'
        ],
        'process_steps': [
            ('Lifestyle Wardrobe Audit', 'We measure your garments, hanging requirements, and bedroom clearance zones.'),
            ('Ergonomic 3D Layout', 'Detailed internal drawer, shelf, and locker division tailored to your preferences.'),
            ('Precision Crafting & Assembly', 'Factory cut carcass, zero-dust edge banding, and flawless on-site alignment.')
        ],
        'gallery': [
            ('/assets/images/portfolio-bedroom.webp', 'Floor-to-Ceiling Sliding Wardrobe', 'Panchsheel Park'),
            ('/assets/images/hero-wardrobe.webp', 'Walk-In Closet with Island', 'Jor Bagh, New Delhi'),
            ('/assets/images/portfolio-wardrobe-2.webp', 'Fluted Charcoal Bedroom Suite', 'Gurugram Sector 42'),
            ('/assets/images/portfolio-fullhome.webp', 'Integrated Dressing Table & Wardrobe', 'Civil Lines'),
            ('/assets/images/portfolio-living.webp', 'Minimalist Handleless Wardrobe', 'Noida Sector 15'),
            ('/assets/images/service-wardrobe.webp', 'Bronze Glass Shutter Master Almirah', 'Hauz Khas Enclave')
        ],
        'pricing': [
            ('Economy Tier', '₹35,000 – ₹65,000 / Wardrobe', ['Commercial Grade Plywood', '1mm Matte Laminates', 'Standard Soft-Close Hinges', 'Hinged Shutter Configuration', 'Quality Audit & Handover']),
            ('Standard Tier', '₹75,000 – ₹1.4 Lakh / Wardrobe', ['BWP Marine Grade Plywood', 'High-Gloss Acrylic or Fluted Texture', 'Hettich Top-Hung Sliding Channels', 'Internal LED Profile Strips', 'Precision Joinery & Care Guide']),
            ('Luxury Bespoke', '₹1.5 Lakh – ₹3 Lakh+ / Suite', ['HDMR & Smoked Veneer Finish', 'Tinted Glass Shutters with Gold Aluminum Profile', 'Full Walk-in Closet Layout', 'Biometric Lockers & Velvet Inserts', 'Master Craftsman Detailing'])
        ],
        'faqs': [
            ('Which is better for Delhi bedrooms: sliding or hinged wardrobes?', 'Sliding wardrobes are ideal for rooms where bed-to-wall clearance is under 3 feet since doors do not swing out. Hinged wardrobes offer 100% full view of clothes at once and cost slightly less.'),
            ('How do you prevent tall 8-foot shutters from bending?', 'We install internal aluminum shutter stiffeners and use premium calibrated 18mm ply or HDMR boards, completely preventing warping over time.'),
            ('Can you add a hidden locker or safe inside the wardrobe?', 'Yes. We frequently integrate biometric or digital fireproof safes concealed behind false drawer fronts or secret plinth drawers.'),
            ('How long does custom wardrobe manufacturing take?', 'Typically 14 to 18 days from 3D approval to on-site assembly and hardware calibration.'),
            ('Do your sliding doors have bottom tracks that gather dirt?', 'No. We prefer top-hung sliding systems that eliminate unsightly floor tracks and operate effortlessly for decades.')
        ],
        'related': [
            ('Bedroom Furniture & Storage', '/bedroom-furniture-delhi/', 'Hydraulic beds, cushioned headboards, study tables, and side consoles.'),
            ('Wall Paneling & TV Units', '/wall-paneling-delhi/', 'Backdrop paneling behind headboards and bedroom TV accent walls.'),
            ('Doors & Partitions', '/doors-partitions-delhi/', 'Sliding fluted glass bedroom partitions and designer interior doors.')
        ]
    },
    {
        'slug': 'wall-paneling-delhi',
        'title': 'Wall Paneling in Delhi | Charcoal & Fluted Panels | Delhi Interior',
        'desc': 'Luxury wall paneling in Delhi. Charcoal panels, fluted MDF slats, PVC/WPC cladding, TV unit backdrops with LED lighting. Free design consultation & site visit.',
        'h1': 'Wall Paneling & TV Units in Delhi',
        'sub': 'Turn plain plaster walls into architectural masterpieces with charcoal panels, fluted acoustic slats, natural veneer, and floating media consoles.',
        'hero_img': '/assets/images/service-paneling.webp',
        'alt': 'Charcoal fluted wall paneling in living room by Delhi Interior Delhi',
        'overview_h2': 'Architectural Depth. Ambient Lighting. Flawless Finish.',
        'overview_p1': 'Bare, flat walls make even large rooms feel uninspired. Wall paneling introduces texture, shadow lines, acoustic dampening, and high-end residential luxury. At Delhi Interior, we specialize in seamless wall treatments — from deep charcoal louvers and fluted MDF slats to book-matched Italian veneer cladding with integrated warm LED illumination.',
        'overview_p2': 'Our floating TV unit backdrops are engineered with 100% concealed cable management ducts, so your set-top boxes, gaming consoles, and soundbars float effortlessly without a single visible cord.',
        'checklist': [
            'Charcoal Polymer Moisture-Proof Slats',
            'Precision CNC Fluted MDF & HDMR Acoustic Paneling',
            'Natural Teak, Walnut & Oak Veneer Cladding with PU Coat',
            'Floating TV Unit Backdrops with Concealed Wire Channels',
            'Integrated 3000K Warm LED Profile & Silicone Cove Lights',
            'Italian Calacatta & Portoro Quartz TV Backdrops',
            'WPC Exterior & Balcony Weatherproof Wall Cladding',
            'Acoustic Felt Sound-Dampening Wall Substrates',
            'Concealed Push-to-Open Media Drawers',
            'Bronze Mirror & Brushed Brass Inlay Metal Strips'
        ],
        'process_steps': [
            ('Wall Leveling & Conduit Prep', 'Laser checking wall plumbness and routing all electrical and audio-visual conduits.'),
            ('Substrate Grid Framing', 'Installing moisture-barrier treated wooden battens for thermal expansion buffer.'),
            ('Panel Cladding & Illumination', 'Precision panel jointing, shadow line alignment, and ambient LED testing.')
        ],
        'gallery': [
            ('/assets/images/portfolio-tvunit.webp', 'Fluted Charcoal TV Backdrop', 'Golf Course Road, Gurugram'),
            ('/assets/images/service-paneling.webp', 'Book-Matched Teak Veneer Wall', 'Vasant Kunj'),
            ('/assets/images/portfolio-living.webp', 'Geometric Brass & Veneer Feature Wall', 'New Friends Colony'),
            ('/assets/images/portfolio-office.webp', 'Home Office Acoustic Paneling', 'Noida Expressway'),
            ('/assets/images/portfolio-dining.webp', 'Dining Area Fluted Paneling with Sconces', 'Safdarjung Enclave'),
            ('/assets/images/portfolio-fullhome.webp', 'Master Bedroom Headboard Cladding', 'Greater Kailash I')
        ],
        'pricing': [
            ('PVC / WPC Slat Paneling', '₹180 – ₹280 / sq. ft.', ['Waterproof PVC Slat Boards', 'Variety of Woodgrain & Charcoal Finishes', 'Quick 2-Day Installation', 'Quality Audit & Handover']),
            ('Fluted MDF & Duco Paint', '₹350 – ₹550 / sq. ft.', ['High Density Moisture Resistant MDF', 'Custom Flute Spacing (12mm / 25mm)', 'Matte PU / Duco Polish Finish', 'Concealed LED Channels & Millwork']),
            ('Luxury Veneer & Metal Inlay', '₹650 – ₹1,200 / sq. ft.', ['Imported Natural Wood Veneers', 'Brushed Brass / Rose Gold PVD Inlays', 'Italian Quartz Floating Console Base', 'Master Craftsman Detailing'])
        ],
        'faqs': [
            ('Can charcoal panels handle Delhi humidity and rainy seasons?', 'Yes. High quality charcoal panels are manufactured from polymer and coal powder composites that are 100% waterproof, termite-proof, and impervious to weather fluctuations.'),
            ('Will all wires behind the TV unit truly be hidden?', 'Yes, completely. We install concealed PVC conduits inside the paneling substrate for HDMI, power, and optical cables before mounting the TV.'),
            ('How long does it take to panel a standard living room wall?', 'Typically 2 to 4 days, minimizing any disruption to your home.'),
            ('Are fluted panels difficult to keep clean from dust?', 'Not at all. Standard micro-fiber dusting or a soft vacuum attachment keeps the vertical grooves pristine. Our panels have smooth anti-static coatings.'),
            ('Can you mount heavy 75-inch or 85-inch TVs on the paneling?', 'Yes. We anchor heavy-duty structural steel brackets directly into the civil masonry behind the paneling to safely support any display size.')
        ],
        'related': [
            ('False Ceiling Design', '/false-ceiling-delhi/', 'Gypsum cove ceilings and magnetic track lights that pair with wall paneling.'),
            ('Painting & Polishing', '/painting-polishing-delhi/', 'PU and Duco finishes that match your custom paneling palette.'),
            ('Doors & Partitions', '/doors-partitions-delhi/', 'Coordinated wooden interior doors and fluted partition screens.')
        ]
    },
    {
        'slug': 'false-ceiling-delhi',
        'title': 'False Ceiling in Delhi | Gypsum & POP Ceiling Design | Delhi Interior',
        'desc': 'Designer false ceiling contractors in Delhi. Gypsum ceilings, cove lighting, magnetic track lights, wooden rafters. High-end finish. Free site estimate.',
        'h1': 'False Ceiling Design & Lighting in Delhi',
        'sub': 'Sculptural gypsum ceilings, concealed cove lighting, and magnetic architectural tracks engineered to transform your room ambiance.',
        'hero_img': '/assets/images/service-ceiling.webp',
        'alt': 'Designer false ceiling installation by Delhi Interior in Delhi',
        'overview_h2': 'Architectural False Ceilings with Heavy-Duty G.I. Framing.',
        'overview_p1': 'The ceiling is the largest unobstructed surface in any room. A thoughtfully designed false ceiling hides unsightly AC drain pipes and electrical conduits while serving as the canvas for layered, glare-free architectural lighting. We use Saint-Gobain Gyproc certified gypsum boards and heavy-gauge galvanized steel framework to ensure zero sagging, cracking, or surface blemishes.',
        'overview_p2': 'Whether you seek minimalist peripheral coves, acoustic wooden baffle rafters, or ultra-modern recessed magnetic track lights, our master ceiling teams execute with laser-guided precision.',
        'checklist': [
            'Saint-Gobain Gyproc Certified 12.5mm Gypsum Sheets',
            'Heavy-Duty Galvanized Steel Framing (G.I. Channels)',
            'Seamless Fiber-Mesh Taping & Anti-Crack Jointing',
            'Concealed Warm 3000K Cove Lighting Troughs',
            'Ultra-Slim Recessed Magnetic Track Light Systems',
            'Wooden Slat Baffles & CNC Accent Insets',
            'Concealed Ductable & Cassette AC Integration',
            'Double-Coat Primer with Ultra-Smooth Matte Ceiling Finish',
            'Acoustic Sound Insulation Mineral Wool Infill Options',
            'Laser-Leveled Elevation Across All Rooms'
        ],
        'process_steps': [
            ('Reflected Ceiling Plan (RCP)', 'Architectural lighting layout and fan/AC position mapping in 3D.'),
            ('Precision G.I. Framework', 'Laser-leveled hanging grid anchoring into RCC slab with heavy fasteners.'),
            ('Board Fixing & Seamless Putty', 'Double-taped gypsum installation, smooth sanding, and ambient light commissioning.')
        ],
        'gallery': [
            ('/assets/images/service-ceiling.webp', 'Minimalist Peripheral Cove Ceiling', 'Mohammadpur, South Delhi'),
            ('/assets/images/portfolio-living.webp', 'Magnetic Track & Sconce Lighting', 'Gulmohar Park'),
            ('/assets/images/portfolio-dining.webp', 'Dining Chandelier Coffer Ceiling', 'DLF Phase 1, Gurugram'),
            ('/assets/images/portfolio-bedroom.webp', 'Master Bedroom Floating Ceiling', 'Vasant Vihar'),
            ('/assets/images/portfolio-office.webp', 'Acoustic Wooden Baffle Ceiling', 'Noida Sector 44'),
            ('/assets/images/portfolio-fullhome.webp', 'Turnkey Modern Luxury Ceiling', 'Sundar Nagar')
        ],
        'pricing': [
            ('Standard Gypsum Perimeter', '₹95 – ₹130 / sq. ft.', ['Saint-Gobain Gyproc Sheets', 'G.I. Framing & Mesh Jointing', 'Concealed Single Cove Trough', 'Quality Audit & Handover']),
            ('Designer Multi-Level Cove', '₹140 – ₹210 / sq. ft.', ['Multi-Tier Level Drops', 'Dual Warm/Neutral Cove Troughs', 'Magnetic Track Inset Channels', 'Reinforced Structural Joinery']),
            ('Luxury Architectural Wood & Acoustic', '₹260 – ₹450 / sq. ft.', ['Veneer / Wooden Baffle Inlays', 'Acoustic Rockwool Insulation Core', 'Complete Lighting Integration', 'Bespoke Studio Detailing'])
        ],
        'faqs': [
            ('Does a false ceiling reduce room height drastically?', 'A standard peripheral cove ceiling only drops 5 to 6 inches along the borders, leaving the central ceiling at full height. It actually makes the room feel taller through uplighting.'),
            ('How do you prevent cracks appearing along false ceiling joints?', 'We use original Gyproc fiber tape with specialized jointing compounds, applied in 3 progressive coats to absorb thermal micro-movements.'),
            ('Can ceiling fans be mounted on a false ceiling?', 'Fans are never anchored into the gypsum board. We install heavy structural steel down-rods securely fastened directly to the RCC slab above.'),
            ('How long does a 3BHK false ceiling project take?', 'Typically 10 to 14 days for framing, boarding, jointing, and primer prep.'),
            ('Can we integrate smart ambient lights with mobile app controls?', 'Yes. We regularly install Wi-Fi and Zigbee compatible CCT tunable strip lights that you can dim or schedule from your phone.')
        ],
        'related': [
            ('Plumbing & Electrical', '/plumbing-electrical-delhi/', 'Concealed wiring, automation switches, and heavy electrical load planning.'),
            ('Painting & Polishing', '/painting-polishing-delhi/', 'Flawless ceiling painting and wall surface preparation.'),
            ('Wall Paneling & TV Units', '/wall-paneling-delhi/', 'Seamless wall-to-ceiling transitions with matching wood textures.')
        ]
    },
    {
        'slug': 'full-home-interior-delhi',
        'title': 'Full Home Interior in Delhi | 2BHK 3BHK 4BHK Turnkey | Delhi Interior',
        'desc': 'Complete turnkey full home interior designers in Delhi NCR. Structured milestone delivery. In-house civil, carpentry, electrical & modular. Master craftsmanship.',
        'h1': 'Full Home Turnkey Interiors in Delhi',
        'sub': 'Complete turnkey home transformation from bare shell to move-in ready. Structured milestone delivery with transparent itemized BOQ.',
        'hero_img': '/assets/images/service-fullhome.webp',
        'alt': 'Full 3BHK home interior by Delhi Interior Delhi',
        'overview_h2': 'One Team. Zero Subcontracting. Total Peace of Mind.',
        'overview_p1': 'Coordinating separate carpenters, civil masons, painters, electricians, and plumbers is exhausting and inevitably leads to delays and finger-pointing. At Delhi Interior, our turnkey service places your entire home under one dedicated project manager and an elite in-house team.',
        'overview_p2': 'From structural civil redesign and Italian marble flooring to bespoke modular kitchens, custom wardrobes, false ceilings, and ambient lighting, we manage every single stage. You receive daily photo updates and move into your dream home on the exact date agreed upon.',
        'checklist': [
            'Complete Architectural Space Planning & 3D Renders',
            'Civil Modifications, Masonry & Wall Demolition / Addition',
            'Modular Kitchen with Quartz Counter & Premium Hardware',
            'Floor-to-Ceiling Wardrobes for All Bedrooms',
            'Designer Gyproc False Ceilings with Layered Lighting',
            'Full Concealed Electrical Re-wiring & Designer Switchboards',
            'Complete CPVC Plumbing & Luxury Sanitaryware Installation',
            'Italian Marble Flooring / Wooden Floor Carpet Laying',
            'Premium Asian Paints Royale / PU Polished Surfaces',
            'Dedicated Full-Time On-Site Project Manager'
        ],
        'process_steps': [
            ('Vision & Space Planning', 'Initial site audit, family lifestyle interview, and room-by-room 3D walkthroughs.'),
            ('Turnkey Civil & Structural Build', 'Demolition, concealed electrical/plumbing conduits, ceiling framing, and flooring.'),
            ('Modular Install & Snag-Free Handover', 'Furniture assembly, polishing, deep cleaning, and ceremonial key handover.')
        ],
        'gallery': [
            ('/assets/images/portfolio-fullhome.webp', '4BHK Turnkey Residence', 'Defence Colony'),
            ('/assets/images/portfolio-living.webp', 'Living & Dining Great Room', 'Vasant Vihar'),
            ('/assets/images/hero-kitchen.webp', 'Open Kitchen & Lounge', 'Golf Links'),
            ('/assets/images/portfolio-bedroom.webp', 'Master Suite with Walk-In Closet', 'Panchsheel Park'),
            ('/assets/images/portfolio-penthouse.webp', 'Luxury Duplex Penthouse', 'DLF Magnolias, Gurugram'),
            ('/assets/images/service-fullhome.webp', 'Contemporary Family Residence', 'Noida Sector 15')
        ],
        'pricing': [
            ('2BHK Turnkey Interior', '₹7 Lakh – ₹14 Lakh', ['Complete Modular Kitchen', '2 Full Wardrobes & Beds', 'False Ceilings & Lighting', 'Wall Painting & Bath Vanities', 'Milestone Schedule & Handover']),
            ('3BHK Turnkey Interior', '₹12 Lakh – ₹24 Lakh', ['Kitchen with Quartz & Appliances', '3 Custom Wardrobes with Lofts', 'Living Paneling & TV Unit', 'Civil Plumbing & Electrical Revamp', 'Milestone Schedule & Handover']),
            ('4BHK / Villa Luxury Turnkey', '₹22 Lakh – ₹45 Lakh+', ['Italian Marble & Hardwood Flooring', 'Full Modular Woodwork & Bar Unit', 'Automated Smart Lighting & Sound', 'Imported Sanitary & PU Surfaces', 'Dedicated Studio Project Director'])
        ],
        'faqs': [
            ('How long does a complete 3BHK interior take in Delhi?', 'A standard 3BHK turnkey transformation takes 60 to 75 days. We provide a milestone-linked calendar before commencement and adhere strictly to it.'),
            ('Can we live in the house while full interior work is ongoing?', 'For full home civil, electrical, and flooring work, we strongly recommend vacating the property so our teams can work without noise and dust constraints to finish faster.'),
            ('Are electrical appliances and loose furniture included?', 'Our core turnkey packages cover all fixed architectural woodwork, civil, electrical, plumbing, ceiling, and painting. Soft furnishings, appliances, and loose sofas can be curated on request.'),
            ('What is your payment milestone structure?', 'We operate on transparent milestone stages: booking advance, 3D design sign-off, factory production commencement, on-site framework completion, and final handover.'),
            ('What quality assurances do you provide on turnkey work?', 'We conduct detailed multi-point quality audits across all civil, electrical, plumbing, and carpentry installations before handover, accompanied by original manufacturer documentation for certified hardware and materials.')
        ],
        'related': [
            ('Modular Kitchen Design', '/modular-kitchen-delhi/', 'Gourmet cooking spaces designed for Indian culinary requirements.'),
            ('Wardrobe Design in Delhi', '/wardrobe-design-delhi/', 'Custom bedroom wardrobes and space-efficient storage.'),
            ('Process & Milestones', '/process/', 'Explore our 5-stage quality-controlled execution workflow.')
        ]
    },
    {
        'slug': 'bedroom-furniture-delhi',
        'title': 'Custom Woodwork & Carpentry in Delhi | Teak Mandirs & Furniture | Delhi Interior',
        'desc': 'Master custom woodwork & precision carpentry in Delhi NCR. Handcrafted teak mandirs, hydraulic storage beds, study desks, architectural millwork. Master craftsmanship.',
        'h1': 'Custom Woodwork & Precision Carpentry in Delhi',
        'sub': 'Handcrafted solid teakwood pooja mandirs, hydraulic storage beds, ergonomic study desks, and bespoke architectural millwork built by in-house master carpenters.',
        'hero_img': '/assets/images/service-furniture.webp',
        'alt': 'Custom woodwork and master carpentry services in Delhi NCR by Delhi Interior',
        'overview_h2': 'Master Carpentry. Millimeter Precision. Built to Outlast Generations.',
        'overview_p1': 'Standard showroom furniture rarely fits the specific alcoves and room dimensions of Delhi homes, leaving awkward dead zones and built with weak particleboard that sags. At Delhi Interior, our 40+ in-house master carpenters (karigars) operate from our dedicated 10,000 sq. ft. precision facility, crafting bespoke woodwork from calibrated Boiling Water Proof (BWP) 710 marine ply, high-density HDMR, and seasoned Burma Teak.',
        'overview_p2': 'From sacred teakwood pooja mandirs with illuminated CNC jali screens to effortless hydraulic platform beds, custom home office workstations, and bespoke dining consoles, every joint and surface is hand-finished with cabinet-maker perfection.',
        'checklist': [
            'Handcrafted Solid Teakwood & Sheesham Temple Mandirs',
            'Hydraulic Gas-Lift Platform Storage Beds with German Struts',
            'Heavy-Duty 25mm Calibrated Marine Ply Bookshelves (Zero Sag)',
            'Ergonomic L-Shaped Study Workstations with Pop-up Power Docks',
            'Custom Dining Credenzas, Bar Cabinets & Fluted Crockery Units',
            'Concealed Louvered Shoe Consoles with Odor Ventilation',
            'Precision CNC Backlit Jali Screens & Brass Inlay Details',
            'German Soft-Close Tandem Hardware (Blum & Hettich)',
            'Hand-Rubbed Natural Teak Grain PU & Italian Acrylic Polish',
            'Dust-Free Factory Sizing & On-Site Alignment by Master Carpenters'
        ],
        'process_steps': [
            ('Ergonomic Space Analysis', 'Measuring room flow, seated eye levels, reach zones, and storage volume.'),
            ('3D Furniture Customization', 'Personalizing finishes, edge profiles, hardware, and cushion fabrics.'),
            ('In-House Factory Build', 'Carcass precision cutting, edge sealing, and sturdy on-site assembly.')
        ],
        'gallery': [
            ('/assets/images/portfolio-office.webp', 'Ergonomic Home Office Suite', 'Noida Expressway'),
            ('/assets/images/portfolio-bedroom.webp', 'Hydraulic Bed with Fluted Headboard', 'Panchsheel Park'),
            ('/assets/images/portfolio-mandir.webp', 'Bespoke Wooden Pooja Mandir', 'Mohammadpur, South Delhi'),
            ('/assets/images/service-furniture.webp', 'Built-in Study Desk & Bookshelf', 'Vasant Kunj'),
            ('/assets/images/portfolio-dining.webp', 'Luxury Bar & Crockery Cabinet', 'DLF Phase 4, Gurugram'),
            ('/assets/images/portfolio-fullhome.webp', 'Minimalist Shoe Rack Console', 'Greater Kailash II')
        ],
        'pricing': [
            ('Custom Study Table Suite', '₹22,000 – ₹45,000', ['L-Shape / Linear Configuration', 'Keyboard Tray & Cable Grommets', 'Drawers with Soft-Close Channels', 'Quality Audit & Handover']),
            ('Hydraulic Bed & Headboard', '₹38,000 – ₹75,000', ['King / Queen Heavy Duty Carcass', 'German 250N Gas Springs', 'Upholstered Fabric Headboard', 'Reinforced Structural Joinery']),
            ('Luxury Mandir / Bar Unit', '₹45,000 – ₹1.2 Lakh+', ['Teak Wood / Corian Stone Accents', 'CNC Backlit Jali Architecture', 'Glass Display with Profile Lights', 'Bespoke Studio Detailing'])
        ],
        'faqs': [
            ('Can the hydraulic bed be lifted easily by one person?', 'Yes. We calibrate the German gas-lift struts to the exact weight of your mattress, allowing anyone to lift it effortlessly with one hand.'),
            ('Will the study desk have visible wire clutter?', 'No. We install concealed wire organizers, modesty panel channels, and desktop pop-up sockets for laptop chargers and monitors.'),
            ('Can you build customized mandirs with brass bells and CNC jali?', 'Yes. Pooja mandirs are a studio specialty. We incorporate sacred proportions, bells, drawer storage for incense, and warm halo illumination.'),
            ('What wood do you use for heavy bookshelf loads?', 'We use minimum 25mm calibrated BWP plywood or high-density HDMR, ensuring shelves never bend even when packed with heavy encyclopedias.'),
            ('Do you offer on-site fabric selection for headboards?', 'Yes. Our team brings swatch booklets of stain-resistant velvets, leathers, and textured bouclé fabrics directly to your site.')
        ],
        'related': [
            ('Wardrobe Design in Delhi', '/wardrobe-design-delhi/', 'Matching bedroom wardrobes and dressing room consoles.'),
            ('Doors & Partitions', '/doors-partitions-delhi/', 'Wooden room dividers and folding acoustic study doors.'),
            ('Painting & Polishing', '/painting-polishing-delhi/', 'Hand-rubbed PU polish for natural teak and oak surfaces.')
        ]
    },
    {
        'slug': 'doors-partitions-delhi',
        'title': 'Doors & Partitions in Delhi | Sliding Glass & Wooden CNC | Delhi Interior',
        'desc': 'Custom doors & partitions in Delhi. Solid wood main doors, sliding glass dividers, CNC acoustic partitions, pocket doors. Master craftsmanship. Call now.',
        'h1': 'Doors & Architectural Partitions in Delhi',
        'sub': 'Grand solid wood main doors, minimalist sliding glass partitions, and intricate CNC screen dividers engineered with concealed hardware.',
        'hero_img': '/assets/images/service-doors.webp',
        'alt': 'Solid wood main door and glass partition by Delhi Interior in Delhi',
        'overview_h2': 'First Impressions Count. Divide Spaces with Elegance.',
        'overview_p1': 'Your main door sets the tone for your entire home, while modern open-plan apartments require smart spatial dividers that maintain light flow while offering visual privacy. We design and install grand pivot doors, solid teak main doors with digital locks, and sleek aluminum-profile sliding glass partitions.',
        'overview_p2': 'Whether separating a dining area from a living hall or creating an acoustic study partition, our solutions glide silently and seal with architectural precision.',
        'checklist': [
            'Solid Seasoned Teakwood & Walnut Main Doors',
            'Heavy-Duty Pivot Door Systems (Supports 150kg+)',
            'Ultra-Slim Fluted & Frosted Glass Aluminum Partitions',
            'Pocket Sliding Doors that Recess Inside Walls',
            'CNC-Cut Wooden & Metal Lattice Decorative Screens',
            'Architectural Fluted Glass French Double Doors',
            'Sound-Insulated Core Flush Doors for Bedrooms',
            'Concealed Magnetic Latches & Architectural Handles',
            'Smart Digital & Biometric Door Lock Installations',
            'Solid Wood Architraves & Custom Door Frame Casings'
        ],
        'process_steps': [
            ('Aperture Laser Calibration', 'Measuring structural door frame plumb, floor levels, and swing clear arcs.'),
            ('Timber Seasoning & Glass Tempering', 'Kiln-dried hardwoods and toughened safety glass fabrication.'),
            ('Concealed Hardware Fitting', 'Installing soft-close tracks, magnetic locks, and weather seals.')
        ],
        'gallery': [
            ('/assets/images/service-doors.webp', 'Grand Pivot Teak Main Door', 'Vasant Vihar'),
            ('/assets/images/portfolio-living.webp', 'Black Aluminum Fluted Glass Divider', 'Defence Colony'),
            ('/assets/images/portfolio-mandir.webp', 'CNC Mandir Screen Folding Doors', 'Mohammadpur, South Delhi'),
            ('/assets/images/portfolio-bedroom.webp', 'Concealed Pocket Bedroom Door', 'Panchsheel Enclave'),
            ('/assets/images/portfolio-fullhome.webp', 'Louvered Wooden Dining Partition', 'Sundar Nagar'),
            ('/assets/images/portfolio-dining.webp', 'Double French Glass Doors', 'Civil Lines')
        ],
        'pricing': [
            ('Flush Door with Veneer / Laminate', '₹16,000 – ₹28,000 / Door', ['Solid Core Tubular Flush Door', '1mm Laminate / Teak Veneer Facing', 'Concealed Heavy Mortise Lock', 'Quality Audit & Handover']),
            ('Sliding Glass & Aluminum Partition', '₹350 – ₹650 / sq. ft.', ['10mm Toughened Fluted/Clear Glass', 'Ultra-Slim Black Anodized Profile', 'Top-Hung Silent Sliding Channels', 'Certified International Hardware']),
            ('Grand Solid Teak Main Door', '₹45,000 – ₹1.2 Lakh+', ['Seasoned Grade-A CP Teakwood', 'Heavy Pivot Hinge System', 'Multi-Coat Weatherproof PU Polish', 'Bespoke Studio Detailing'])
        ],
        'faqs': [
            ('Do your sliding glass partitions require a track on the floor?', 'No. We use top-hung overhead tracks with concealed ceiling reinforcements. Your floor tile remains completely smooth without tripping hazards.'),
            ('How do you ensure wooden main doors do not swell during Delhi monsoons?', 'We use exclusively kiln-seasoned hardwoods with moisture content under 12%, followed by six protective coats of exterior-grade PU sealers.'),
            ('Can you integrate biometric smart locks on custom doors?', 'Yes. We cut precision cavities for Yale, Godrej, Hafele, and Samsung digital smart locks with fingerprint and PIN access.'),
            ('Does fluted glass provide adequate visual privacy?', 'Fluted glass diffuses light beautifully while obscuring clear visibility, making it the perfect choice between dining, living, and kitchen zones.'),
            ('How long does door fabrication and polish take?', 'Approximately 10 to 14 days, with on-site installation completed in a single day per door.')
        ],
        'related': [
            ('Wall Paneling & TV Units', '/wall-paneling-delhi/', 'Complementary wooden wall paneling and acoustic backdrops.'),
            ('Painting & Polishing', '/painting-polishing-delhi/', 'High-end PU and Duco polishing for interior door frames.'),
            ('Modular Kitchen Design', '/modular-kitchen-delhi/', 'Glass pantry partitions and sliding kitchen entrance doors.')
        ]
    },
    {
        'slug': 'painting-polishing-delhi',
        'title': 'Painting & Polishing in Delhi | PU Polish & Duco Paint | Delhi Interior',
        'desc': 'Master painting & polishing contractors in Delhi. PU polishing, Duco paint, texture walls, veneer polishing. Flawless mirror finish. Call for quote.',
        'h1': 'Paints, Polish & Surface Finishing in Delhi',
        'sub': 'Flawless Italian PU polishing, mirror-finish Duco paint, luxury texture walls, and natural veneer restoration by master finish artisans.',
        'hero_img': '/assets/images/service-painting.webp',
        'alt': 'PU polishing and luxury wall painting by Delhi Interior in Delhi',
        'overview_h2': 'The Final Finish That Defines True Luxury Quality.',
        'overview_p1': 'The difference between average interior work and a luxury editorial home lies entirely in the surface finish. Uneven paint brush marks, bubbling veneer, or orange-peel paint surfaces immediately destroy an otherwise expensive project. At Delhi Interior, our finishing masters use spray booths and dust-controlled environments.',
        'overview_p2': 'We apply genuine Italian Polyurethane (PU) coatings, high-gloss and dead-matte Duco lacquers, and metallic texture wall designs using Asian Paints Royale and Sirca Italian polishes.',
        'checklist': [
            'Genuine Italian Sirca & ICA Polyurethane (PU) Coatings',
            'Mirror High-Gloss & Velvet Matte Duco Spray Finishes',
            'Natural Teak, Oak & Walnut Veneer Hand-Rubbed Polishing',
            'Level-5 Gypsum Wall Putty Preparation & Sanding',
            'Asian Paints Royale Luxury Emulsion Application',
            'Velvet, Stucco & Concrete Texture Accent Walls',
            'Anti-Fungal & Anti-Efflorescence Primer Treatment',
            'Seamless Designer Wallpaper & Metallic Inlay Application',
            'Epoxy Floor Grouting & Polyurethane Floor Sealers',
            'Dust-Controlled Spray Equipment & Site Masking'
        ],
        'process_steps': [
            ('Surface Stripping & Putty Base', 'Applying waterproof acrylic putty and sanding with fine 320-grit abrasives.'),
            ('Primer & Undercoat Sealing', 'Two coats of specialized sealer to prevent timber sap bleed and moisture seepage.'),
            ('Multi-Coat Spray & Buffing', '3 to 5 spray coats of PU/Duco with machine buffing to achieve optical mirror flatness.')
        ],
        'gallery': [
            ('/assets/images/service-painting.webp', 'Mirror-Finish PU Kitchen Shutters', 'Chanakyapuri'),
            ('/assets/images/portfolio-living.webp', 'Concrete Texture Accent Wall', 'Greater Kailash I'),
            ('/assets/images/portfolio-tvunit.webp', 'Natural Teak Hand-Rubbed Polish', 'Golf Course Road'),
            ('/assets/images/portfolio-dining.webp', 'Velvet Matte Duco Bedroom Wall', 'Vasant Vihar'),
            ('/assets/images/portfolio-bedroom.webp', 'Seamless Metallic Leaf Wallpaper', 'Sundar Nagar'),
            ('/assets/images/portfolio-fullhome.webp', 'Level-5 Royale Emulsion Interior', 'Defence Colony')
        ],
        'pricing': [
            ('Royale Interior Painting', '₹28 – ₹45 / sq. ft.', ['Full Acrylic Putty Sanding', 'Asian Paints Royale Emulsion', 'Roller Stipple-Free Finish', 'Quality Audit & Handover']),
            ('Duco Lacquer Spray Finish', '₹160 – ₹280 / sq. ft.', ['Automotive Grade Acrylic Lacquer', 'Matte or Satin Sheen', 'Spray Applied in Clean Environment', 'High-Durability Finish']),
            ('Italian PU (Polyurethane)', '₹290 – ₹550 / sq. ft.', ['Sirca / ICA Italian Polyurethane', '100% Scratch & Chemical Proof', 'Mirror Gloss or Dead Matte Buff', 'Italian PU Buff & Inspection'])
        ],
        'faqs': [
            ('What is the difference between PU polish and regular Melamine polish?', 'Melamine turns yellow over time and stains easily from water rings. Italian PU (Polyurethane) remains crystal clear, is completely non-yellowing, and offers 5x superior scratch and heat resistance.'),
            ('Does Duco paint emit strong fumes inside the house?', 'During active spray application there is an odor, which is why we exhaust the space with commercial blowers. Once cured within 24 hours, the surface is completely non-toxic and odor-free.'),
            ('How do you fix peeling wall paint caused by moisture seepage?', 'We never paint over active dampness. We identify the source, apply specialized chemical crystalline waterproofing primers, let the masonry cure, and then proceed with breathable finish coats.'),
            ('Can you match exact paint shades from luxury international catalogues?', 'Yes. Using computerized spectrophotometer tinting, we match precise shades from Farrow & Ball, Benjamin Moore, or Asian Paints collections.'),
            ('How long does painting a 3BHK apartment take?', 'Surface prep and painting typically takes 7 to 10 days, ensuring adequate drying time between progressive coats.')
        ],
        'related': [
            ('Wall Paneling & TV Units', '/wall-paneling-delhi/', 'Charcoal panels and fluted wall features that pair with paint tones.'),
            ('Modular Kitchen Design', '/modular-kitchen-delhi/', 'PU lacquered and anti-scratch acrylic kitchen shutters.'),
            ('False Ceiling Design', '/false-ceiling-delhi/', 'Seamless level-5 gypsum ceiling painting and cove finishes.')
        ]
    },
    {
        'slug': 'plumbing-electrical-delhi',
        'title': 'Plumbing & Electrical in Delhi | Turnkey MEP Contractors | Delhi Interior',
        'desc': 'Complete concealed plumbing & electrical contractors in Delhi. Heavy wiring, profile lighting, sanitary fittings, geysers. Certified team. Call now.',
        'h1': 'Concealed Plumbing & Electrical in Delhi',
        'sub': 'Complete concealed conduit re-wiring, architectural lighting circuits, CPVC plumbing, sanitaryware, and bathroom waterproofing.',
        'hero_img': '/assets/images/service-electrical.webp',
        'alt': 'Concealed electrical and plumbing installations by Delhi Interior in Delhi',
        'overview_h2': 'The Hidden Arteries of a Flawless Home.',
        'overview_p1': 'The most expensive interior surfaces are only as good as the hidden civil, electrical, and plumbing infrastructure behind them. A single leaky pipe joint inside a wall can ruin hundreds of thousands of rupees worth of custom woodwork and Italian marble.',
        'overview_p2': 'At Delhi Interior, our licensed in-house master electricians and plumbers manage complete MEP (Mechanical, Electrical, Plumbing) redesigns. We test every water supply line under high hydraulic pressure for 48 hours and megger-test all electrical circuits before closing any walls.',
        'checklist': [
            'FR-LSH (Fire Retardant Low Smoke) Pure Copper Wiring (Polycab / Havells)',
            'Dedicated Heavy Load Circuits for ACs, Geysers & Induction Hobs',
            'Architectural Modular Switchboards (Legrand / Schneider / Norisys)',
            'Multi-Zone Dimmable & Ambient Cove Lighting Loops',
            'Pressure-Tested CPVC Cold & Hot Water Supply Piping (Astral / Ashirvad)',
            'Sound-Dampening SWR PVC Drainage with Anti-Odor Floor Traps',
            'Concealed Cisterns & Wall-Hung WC Fittings (Grohe / Kohler / Jaquar)',
            'Diverters, Thermostatic Rain Showers & Body Jet Plumbing',
            'Polymer-Modified Multi-Layer Bathroom Waterproofing',
            'Earthing Pit Installation & MCB / RCCB Distribution Box Upgrades'
        ],
        'process_steps': [
            ('Circuit & Pressure Load Design', 'Calculating wattages, phase distribution, and water pressure requirements.'),
            ('Concealed Wall Chasing & Piping', 'Precision laser wall chasing and chemical joint solvent welding.'),
            ('48-Hour Pressure Testing', 'Hydraulic testing at 10 bar pressure and electrical insulation certification.')
        ],
        'gallery': [
            ('/assets/images/service-electrical.webp', 'Architectural Electrical Switchgear', 'Vasant Kunj'),
            ('/assets/images/portfolio-bathroom.webp', 'Concealed Rain Shower & Vanity', 'Greater Kailash II'),
            ('/assets/images/hero-kitchen.webp', 'Concealed Island Kitchen Plumbing', 'Golf Links'),
            ('/assets/images/portfolio-living.webp', 'Multi-Circuit Cove Lighting Setup', 'Panchsheel Park'),
            ('/assets/images/portfolio-office.webp', 'Structured Data & Power Outlets', 'Gurugram Sector 54'),
            ('/assets/images/portfolio-fullhome.webp', 'Luxury Bathroom Turnkey Renovation', 'Defence Colony')
        ],
        'pricing': [
            ('Electrical Point Rewiring', '₹650 – ₹950 / point', ['Polycab FRLS Copper Wire', 'Heavy G.I. Concealed Box', 'Labor for Wall Chasing & Plaster', 'Quality Audit & Handover']),
            ('Turnkey Bathroom Plumbing', '₹28,000 – ₹55,000 / bath', ['Astral CPVC Piping Lines', 'Concealed Diverter & Flush Tank', '48-Hour Pressure Testing', 'Hydro-Static Pressure Tested']),
            ('Full 3BHK MEP Overhaul', '₹1.8 Lakh – ₹3.5 Lakh', ['Complete Rewiring + Distribution Board', 'All Bathroom & Kitchen Plumbing', 'Multi-Layer Polymer Waterproofing', 'Bespoke Studio Detailing'])
        ],
        'faqs': [
            ('How do you ensure that newly tiled bathrooms will not leak into ceilings below?', 'We apply a double-layer chemical crystalline waterproof slurry followed by an elastic acrylic fiber membrane across the entire sunken slab and 12 inches up the walls. We flood-test the bathroom for 72 hours before tiling.'),
            ('Will our electrical wiring support multiple heavy 2-ton inverter ACs running simultaneously?', 'Yes. We run independent, unshared 4 sq. mm fire-retardant copper wires with dedicated MCB breakers directly from the main distribution panel for each air conditioner.'),
            ('Can you install smart automation switches that work with Alexa and Google Home?', 'Yes. We integrate smart touch panels and concealed relay modules from Legrand, Schneider, or smart Wi-Fi systems into standard switch boxes.'),
            ('Do you provide high-pressure booster pump installations for luxury rain showers?', 'Yes. Multi-function rain and mist showers require 2.5 to 3.5 bar pressure, so we size and install silent hydro-pneumatic booster systems.'),
            ('How long does full electrical and plumbing overhaul take for a 3BHK?', 'Typically 12 to 16 days, scheduled alongside initial civil masonry before false ceilings and modular woodwork begin.')
        ],
        'related': [
            ('Modular Kitchen Design', '/modular-kitchen-delhi/', 'Sanitary and electrical cutouts for dishwashers, hobs, and RO systems.'),
            ('False Ceiling Design', '/false-ceiling-delhi/', 'Concealed ceiling wiring and magnetic architectural tracks.'),
            ('Full Home Turnkey Interiors', '/full-home-interior-delhi/', 'Comprehensive turnkey home execution covering all services.')
        ]
    }
]

for s in SERVICES_DATA:
    page_dir = s['slug']
    os.makedirs(page_dir, exist_ok=True)
    html_file = os.path.join(page_dir, 'index.html')

    schema = {
        '@context': 'https://schema.org',
        '@type': 'BreadcrumbList',
        'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': 'https://delhiinterior.com/'},
            {'@type': 'ListItem', 'position': 2, 'name': s['h1'], 'item': f'https://delhiinterior.com/{s["slug"]}/'}
        ]
    }

    checklist_html = '\n'.join([f'<div class="checklist-item"><span class="check">✓</span><span>{item}</span></div>' for item in s['checklist']])

    process_html = '\n'.join([
        f'<div class="process-step"><div class="step-circle">{idx+1}</div><h4>{title}</h4><p>{desc}</p></div>'
        for idx, (title, desc) in enumerate(s['process_steps'])
    ])

    gallery_html = '\n'.join([
        f'<div class="portfolio-card"><picture><source srcset="{img}" type="image/webp"><img src="{img.replace(".webp", ".jpg")}" alt="{title} by Delhi Interior in Delhi" width="800" height="600" loading="lazy"></picture><div class="portfolio-overlay"><h3>{title}</h3><p>{loc}</p></div></div>'
        for img, title, loc in s['gallery']
    ])

    pricing_html = '\n'.join([
        f'<div class="price-tier-card {"featured" if idx == 1 else ""}"><h3>{tier_name}</h3><div class="price">{price}</div><ul>' +
        ''.join([f'<li>{feat}</li>' for feat in feats]) +
        f'</ul><a href="/contact/" class="btn {"btn-secondary" if idx == 1 else "btn-primary"}">Get Estimate</a></div>'
        for idx, (tier_name, price, feats) in enumerate(s['pricing'])
    ])

    faq_html = '\n'.join([
        f'<div class="faq-item"><button class="faq-question" aria-expanded="false"><span>{q}</span><span class="faq-toggle">+</span></button><div class="faq-answer"><div class="faq-answer-inner">{a}</div></div></div>'
        for q, a in s['faqs']
    ])

    related_html = '\n'.join([
        f'<div class="blog-card"><div class="blog-card-body"><h3>{rtitle}</h3><p>{rdesc}</p><a href="{rlink}" class="blog-read-link">Explore Service</a></div></div>'
        for rtitle, rlink, rdesc in s['related']
    ])

    page_content = f'''<!DOCTYPE html>
<html lang="en-IN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>{s['title']}</title>
  <meta name="description" content="{s['desc']}">
  <link rel="canonical" href="https://delhiinterior.com/{s['slug']}/">

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:title" content="{s['title']}">
  <meta property="og:description" content="{s['desc']}">
  <meta property="og:url" content="https://delhiinterior.com/{s['slug']}/">
  <meta property="og:image" content="https://delhiinterior.com/og-image.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:locale" content="en_IN">

  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{s['title']}">
  <meta name="twitter:description" content="{s['desc']}">
  <meta name="twitter:image" content="https://delhiinterior.com/og-image.jpg">

  <!-- Favicons -->
  <link rel="icon" href="/favicon.ico" sizes="any">
  <link rel="icon" href="/favicon-32x32.png" type="image/png">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <link rel="manifest" href="/site.webmanifest">

  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400;1,500;1,600&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500;9..40,600&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="/assets/css/style.css">

  <!-- BreadcrumbList Schema -->
  <script type="application/ld+json">
{json.dumps(schema, indent=2)}
  </script>
</head>
<body>
  <a href="#main-content" class="skip-link">Skip to main content</a>

  <!-- Announcement Bar -->
  <aside id="announcement-bar" aria-label="Announcement">
    <div class="bar-content">
      ✦ Free Design Consultation with every project · Call +91 96438 17099 · Open 24 Hours (7 Days a Week) ✦
    </div>
    <button class="close-btn" aria-label="Dismiss announcement bar">✕</button>
  </aside>

  <!-- Navigation Bar -->
  <header class="site-header" role="banner">
    <div class="container nav-container">
      <a href="/" class="site-logo" aria-label="Delhi Interior Home">
        Delhi <span class="logo-accent">Interior</span>
      </a>
      <nav class="main-navigation" aria-label="Main navigation">
        <ul class="nav-links">
          <li><a href="/modular-kitchen-delhi/" class="active">Services</a></li>
          <li><a href="/portfolio/">Portfolio</a></li>
          <li><a href="/process/">Process</a></li>
          <li><a href="/blog/">Blog</a></li>
          <li><a href="/about/">About</a></li>
          <li><a href="/contact/">Contact</a></li>
        </ul>
      </nav>
      <div class="nav-right">
        <a href="tel:+919643817099" class="nav-phone" aria-label="Call +91 96438 17099">
          <svg viewBox="0 0 24 24"><path d="M6.62 10.79c1.44 2.83 3.76 5.15 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
          +91 96438 17099
        </a>
        <a href="/contact/" class="btn btn-secondary">Free Consultation</a>
        <button class="hamburger" aria-label="Open navigation menu">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
  </header>

  <!-- Mobile Menu -->
  <div id="mobile-menu" class="mobile-menu-overlay" aria-modal="true" role="dialog">
    <div class="mobile-menu-header">
      <div class="site-logo">Delhi <span class="logo-accent">Interior</span></div>
      <button class="mobile-menu-close close-btn" aria-label="Close navigation menu">✕</button>
    </div>
    <ul class="mobile-nav-links">
      <li><a href="/" onclick="closeMobileMenu()">Home</a></li>
      <li><a href="/modular-kitchen-delhi/" onclick="closeMobileMenu()">Services</a></li>
      <li><a href="/portfolio/" onclick="closeMobileMenu()">Portfolio</a></li>
      <li><a href="/process/" onclick="closeMobileMenu()">Process</a></li>
      <li><a href="/blog/" onclick="closeMobileMenu()">Blog</a></li>
      <li><a href="/about/" onclick="closeMobileMenu()">About Us</a></li>
      <li><a href="/contact/" onclick="closeMobileMenu()">Contact</a></li>
    </ul>
    <div class="mobile-menu-footer">
      <p>F-128/4, Mohammadpur, New Delhi 110066<br>Open 24 Hours</p>
      <a href="tel:+919643817099" class="btn btn-secondary">Call +91 96438 17099</a>
    </div>
  </div>

  <!-- WhatsApp Float -->
  <a href="https://wa.me/919643817099?text=Hi%2C+I+am+interested+in+{s['slug'].replace('-','+')}+services." class="whatsapp-float" target="_blank" rel="noopener noreferrer" aria-label="Chat on WhatsApp">
    <svg viewBox="0 0 24 24"><path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2m.01 1.67c2.2 0 4.26.86 5.82 2.42a8.225 8.225 0 0 1 2.41 5.83c0 4.54-3.7 8.24-8.24 8.24-1.48 0-2.93-.4-4.2-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.196 8.196 0 0 1-1.26-4.38c0-4.54 3.7-8.24 8.24-8.24m4.52 11.66c-.19-.09-1.12-.55-1.3-.61-.17-.07-.3-.1-.43.1-.12.19-.48.61-.59.73-.11.12-.22.14-.41.05-.19-.09-.8-.29-1.53-.94-.57-.51-.95-1.13-1.06-1.32-.11-.19-.01-.3.08-.39.09-.08.19-.22.29-.33.09-.11.12-.19.19-.31.06-.12.03-.24-.01-.33-.05-.09-.43-1.04-.6-1.42-.16-.38-.32-.33-.44-.33h-.37c-.13 0-.34.05-.52.24-.18.19-.69.67-.69 1.64s.71 1.9 1.01 2.3c.3.4 1.92 2.93 4.65 4.11.65.28 1.16.45 1.55.58.65.21 1.25.18 1.72.11.53-.08 1.62-.66 1.85-1.3.23-.64.23-1.19.16-1.3-.06-.11-.23-.18-.42-.27z"/></svg>
    <span class="whatsapp-tooltip">Chat Now</span>
  </a>

  <!-- Mobile Sticky CTA -->
  <aside class="sticky-mobile-cta" aria-label="Quick mobile contact actions">
    <div class="cta-btn-group">
      <a href="tel:+919643817099" class="cta-btn btn-call">Call Now</a>
      <a href="https://wa.me/919643817099?text=Hi%2C+I+am+interested+in+{s['slug'].replace('-','+')}+services." class="cta-btn btn-wa" target="_blank" rel="noopener noreferrer">WhatsApp</a>
    </div>
  </aside>

  <!-- Main Content -->
  <main id="main-content">

    <!-- 1. Hero (60vh) -->
    <section class="inner-hero">
      <div class="container">
        <nav class="breadcrumbs" aria-label="Breadcrumb">
          <a href="/">Home</a> / <a href="/modular-kitchen-delhi/">Services</a> / <span>{s['h1']}</span>
        </nav>
        <h1>{s['h1']}</h1>
        <p>{s['sub']}</p>
        <a href="/contact/" class="btn btn-secondary">Get Free Quote</a>
      </div>
    </section>

    <!-- 2. Featured Real Photo (480px height) -->
    <div class="container" style="margin-top: -2rem;">
      <div class="featured-service-photo">
        <picture>
          <source srcset="{s['hero_img']}" type="image/webp">
          <img src="{s['hero_img'].replace('.webp', '.jpg')}" alt="{s['alt']}" width="1200" height="480" loading="eager">
        </picture>
      </div>
    </div>

    <!-- 3. Overview Section -->
    <section class="container" style="padding-bottom: 4rem;">
      <span class="gold-line"></span>
      <h2>{s['overview_h2']}</h2>
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 3rem; margin-top: 1.5rem;">
        <p>{s['overview_p1']}</p>
        <p>{s['overview_p2']}</p>
      </div>
    </section>

    <!-- 4. What's Included (Checklist) -->
    <section class="bg-stone" style="padding: 4rem 0;">
      <div class="container">
        <span class="gold-line"></span>
        <h2>What's Included in Every Project</h2>
        <p style="margin-bottom: 2rem;">Every specification is agreed in writing. No substitutions, no cheap shortcuts.</p>
        <div class="checklist-grid">
          {checklist_html}
        </div>
      </div>
    </section>

    <!-- 5. 3-Step Process -->
    <section class="container" style="padding: 5rem 0;">
      <span class="gold-line"></span>
      <h2>Our Seamless Process</h2>
      <div class="process-steps" style="grid-template-columns: repeat(3, 1fr); margin-top: 3rem;">
        {process_html}
      </div>
    </section>

    <!-- 6. Gallery (6 Real Project Photos) -->
    <section class="bg-cream" style="padding: 5rem 0;">
      <div class="container">
        <span class="gold-line"></span>
        <h2>Recent Completed Projects in Delhi</h2>
        <p style="margin-bottom: 2.5rem;">A glimpse of our recently executed work across South Delhi, Gurugram, and Noida.</p>
        <div class="portfolio-full-grid">
          {gallery_html}
        </div>
      </div>
    </section>

    <!-- 7. Starting Price Guide (3 Tiers) -->
    <section class="container" style="padding: 5rem 0;">
      <span class="gold-line gold-line-center"></span>
      <h2 style="text-align: center;">Transparent Pricing Guide</h2>
      <p style="text-align: center; margin: 0 auto 1.5rem;">Prices vary by size, room layout, and selected material finish. Contact us for an exact itemized quotation.</p>
      <div class="pricing-tiers-grid">
        {pricing_html}
      </div>
    </section>

    <!-- 8. Service FAQs (5 Questions) -->
    <section class="bg-stone" style="padding: 5rem 0;">
      <div class="container faq-wrap">
        <span class="gold-line gold-line-center"></span>
        <h2 style="text-align: center;">Frequently Asked Questions</h2>
        <div class="faq-list" style="margin-top: 2.5rem;">
          {faq_html}
        </div>
      </div>
    </section>

    <!-- 9. CTA Banner Section -->
    <section class="cta-banner-section bg-navy-primary">
      <div class="container">
        <span class="gold-line gold-line-center"></span>
        <h2>Ready to Start Your Project?</h2>
        <p>Book a free site consultation and 3D design session with our principal design director.</p>
        <div class="cta-buttons">
          <a href="/contact/" class="btn btn-white-dark">Book Free Site Visit</a>
          <a href="https://wa.me/919643817099?text=Hi%2C+I+am+interested+in+{s['slug'].replace('-','+')}+services." class="btn btn-outline-white" target="_blank" rel="noopener noreferrer">Chat on WhatsApp</a>
        </div>
      </div>
    </section>

    <!-- 10. Related Services -->
    <section class="container" style="padding: 5rem 0;">
      <span class="gold-line"></span>
      <h2>Related Interior Services</h2>
      <div class="blog-grid" style="margin-top: 2rem;">
        {related_html}
      </div>
    </section>

  </main>

  <!-- Footer -->
  <footer class="site-footer" role="contentinfo">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-col">
          <div class="site-logo" style="margin-bottom: 1rem;">Delhi <span class="logo-accent">Interior</span></div>
          <p>Premium interior design in Delhi — custom modular kitchens, wardrobes, wall paneling, and full home interiors. Trusted by 500+ homeowners.</p>
        </div>
        <div class="footer-col">
          <h4>Services</h4>
          <ul class="footer-links">
            <li><a href="/modular-kitchen-delhi/">Modular Kitchen</a></li>
            <li><a href="/wardrobe-design-delhi/">Wardrobes &amp; Bedroom</a></li>
            <li><a href="/wall-paneling-delhi/">Wall Paneling &amp; TV Units</a></li>
            <li><a href="/false-ceiling-delhi/">False Ceiling</a></li>
            <li><a href="/full-home-interior-delhi/">Full Home Interior</a></li>
            <li><a href="/bedroom-furniture-delhi/">Woodwork &amp; Carpentry</a></li>
            <li><a href="/doors-partitions-delhi/">Doors &amp; Partitions</a></li>
            <li><a href="/painting-polishing-delhi/">Paints &amp; Polish</a></li>
            <li><a href="/plumbing-electrical-delhi/">Plumbing &amp; Electrical</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Company</h4>
          <ul class="footer-links">
            <li><a href="/about/">About Us</a></li>
            <li><a href="/portfolio/">Portfolio</a></li>
            <li><a href="/process/">Our Process</a></li>
            <li><a href="/blog/">Blog &amp; Guides</a></li>
            <li><a href="/contact/">Get a Quote</a></li>
            <li><a href="/sitemap/">HTML Sitemap</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Get in Touch</h4>
          <div class="footer-contact-info">
            <p><strong>Phone:</strong> <a href="tel:+919643817099">+91 96438 17099</a></p>
            <p><strong>WhatsApp:</strong> <a href="https://wa.me/919643817099" target="_blank" rel="noopener noreferrer">+91 96438 17099</a></p>
            <p><strong>Email:</strong> <a href="mailto:hello@delhiinterior.com">hello@delhiinterior.com</a></p>
            <p>F-128/4, Mohammadpur, New Delhi, Delhi, 110066</p>
          </div>
        </div>
      </div>
      <div class="footer-divider"></div>
      <div class="footer-bottom">
        <div>© <span id="year"></span> Delhi Interior. All rights reserved.</div>
        <div class="footer-legal-links">
          <a href="/privacy-policy/">Privacy Policy</a>
          <a href="/terms-of-service/">Terms of Service</a>
          <a href="/sitemap/">Sitemap</a>
        </div>
      </div>
    </div>
  </footer>

  <aside id="cookie-banner" role="dialog">
    <p>We use cookies to improve your experience and analyse site traffic.</p>
    <div class="cookie-buttons">
      <button id="cookie-accept" class="btn btn-secondary" style="padding: 0.5rem 1.5rem;">Accept</button>
      <button id="cookie-decline" class="btn btn-ghost" style="padding: 0.5rem 1.5rem;">Decline</button>
    </div>
  </aside>

  <script defer src="/assets/js/main.js"></script>
</body>
</html>
'''
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(page_content)
    print(f'Generated: {html_file}')

print('All 9 service pages created.')
