# AGENT RESUME CHECKPOINT

> **Status**: READY FOR PRODUCTION DEPLOYMENT  
> **Timestamp**: 2026-11-16T23:25:00+05:30  
> **Remote Repository**: `https://github.com/officialdelhiinterior/delhi-interior-website.git`  
> **Collaborator**: `anurag9702`  
> **Local Server**: Running on `http://localhost:8000/` via `scripts/server.py`  

---

## 1. Quick Resume Instructions for Future Agents
If your execution is interrupted, resumed, or handed over, follow these exact steps:

1. **Verify Environment**:
   ```bash
   # Confirm workspace directory
   cd c:\Users\anura\.gemini\antigravity\scratch\delhi-interior-website
   
   # Check git status
   git status
   ```

2. **Run Rigorous Audits**:
   ```bash
   python scripts/audit_site.py
   python scripts/audit_buttons_and_interactions.py
   ```
   Both audits **MUST** exit with 0 errors and 0 warnings.

3. **Check Dev Server**:
   Ensure `scripts/server.py` is running on port 8000. If stopped:
   ```bash
   python scripts/server.py
   ```

4. **Verify Live Rendering**:
   Use the `browser` subagent to check `http://localhost:8000/` to ensure no visual regressions.

---

## 2. Invariants & Non-Negotiable Rules

Do **NOT** violate any of the following constraints under any circumstances:

1. **Business Identity**:
   - Name: `Delhi Interior`
   - Address: `F-128/4, Mohammadpur, New Delhi 110066`
   - Phone: `+91 96438 17099` (Call / 24/7)
   - WhatsApp: `wa.me/919643817099`
   - Timing: `Open 24 Hours / 24/7`

2. **Policy Compliance (Strict)**:
   - **ZERO** mentions of `"warranty"`, `"guarantee"`, `"45 days"`, or `"42 days"`.
   - Never reintroduce day-based guarantees or warranty badges.
   - Run `python scripts/scan_forbidden.py` to verify zero violations.

3. **Color System Discipline**:
   - **Primary**: Deep Dark Navy Blue (`#0B2540` / `#0A1626`).
   - **Accent**: Warm Architectural Golden Brass (`#B89058` / `#C5A880`).
   - **Surfaces**: Crisp White (`#FFFFFF`) and Warm Ivory (`#F8F6F0` / `#F8F5EE`).
   - **WhatsApp Green (`#25D366`)**: **STRICTLY AND EXCLUSIVELY** for WhatsApp action buttons (`.whatsapp-float`, `.btn-whatsapp`). Absolutely no other element may be green.

4. **Floating Action Buttons**:
   - Fixed bottom-right corner.
   - The **Call button** (`#0B2540` with golden border) is located directly **ABOVE** the **WhatsApp button** (`#25D366`).

5. **Section Specifications**:
   - **Section 2.5 "Why Choose Us"**: Single elevated white floating box (`.why-choose-floating-box`) with 4 columns over a warm interior bedroom photo background with translucent wash. Centered typography, clean line vector icons, no bottom colored badges.
   - **Section 6.5 "An interior solution for every brief"**: Seamless warm sand container (`#F8F5EE`) with 5 side-by-side columns (`01` to `05`), `Playfair Display` serif typography, and `Request details ↗` links.
   - **Section 6 "Certified Materials"**: Permanently removed. Do **NOT** restore it.

6. **Image Standards**:
   - **NO random stock photos**. All 25 images must be high-resolution, luxury architectural interior photographs matching their labels (Modular Kitchen, Walk-in Wardrobe, Master Carpenters in workshop, Design Studio Team, Backlit Brass Jali Mandir, Fluted Master Suite, TV Unit, Teak Pivot Door, etc.).

---

## 3. Key Generator Scripts (Single Sources of Truth)
If making changes to styling or HTML, update the generator scripts first, then recompile:

- **Styles**: Edit `scripts/generate_master_style.py` then run `python scripts/generate_master_style.py` (writes to `assets/css/style.css`).
- **Homepage**: Edit `scripts/rebuild_complete_site_v3.py` then run `python scripts/rebuild_complete_site_v3.py` (writes to `index.html`).
- **Subpages**:
  - `scripts/build_main_and_utility.py` (About, Contact, Portfolio, Process, Legal, 404)
  - `scripts/update_build_services.py` (9 Service pages)
  - `scripts/update_build_blog.py` (6 Blog pages)

---

## 4. Current State Snapshot
- All 25 HTML pages are valid, responsive, and SEO-optimized.
- All interactive links, buttons, FAQ accordions, and consultation modals are 100% functional.
- All 25 image assets are optimized WebP + JPG files in `assets/images/`.
- Git initialized with origin `https://github.com/officialdelhiinterior/delhi-interior-website.git`.
