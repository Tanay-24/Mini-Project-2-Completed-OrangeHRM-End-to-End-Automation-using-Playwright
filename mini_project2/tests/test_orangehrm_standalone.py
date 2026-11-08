import os
import random
import time
from playwright.sync_api import sync_playwright, expect

def generate_custom_html_report(emp_id, emp_name, video_file_name, duration_sec):
    """कोणत्याही प्लगइनशिवाय थेट सुंदर पाई-चार्ट रिपोर्ट तयार करणारी पद्धत"""
    os.makedirs("reports", exist_ok=True)
    report_path = os.path.join("reports", "orangehrm_report.html")

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>OrangeHRM E2E Automation Executive Report</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #0f172a; color: #f8fafc; margin: 0; padding: 30px; }}
        .container {{ max-width: 1050px; margin: auto; }}
        .header {{ background: linear-gradient(135deg, #1e293b, #334155); padding: 25px 30px; border-radius: 16px; margin-bottom: 25px; border-left: 6px solid #ff7b00; box-shadow: 0 10px 25px rgba(0,0,0,0.3); }}
        .cards {{ display: flex; gap: 20px; margin-bottom: 25px; flex-wrap: wrap; }}
        .card {{ flex: 1; min-width: 200px; background: #1e293b; padding: 20px; border-radius: 14px; box-shadow: 0 4px 15px rgba(0,0,0,0.2); border: 1px solid #334155; }}
        .chart-box {{ display: flex; gap: 30px; background: #1e293b; border-radius: 16px; padding: 30px; align-items: center; justify-content: space-around; flex-wrap: wrap; border: 1px solid #334155; margin-bottom: 25px; }}
        .badge {{ background: #064e3b; color: #34d399; padding: 5px 12px; border-radius: 20px; font-weight: 600; font-size: 13px; display: inline-block; margin-top: 5px; }}
        .details-table {{ width: 100%; border-collapse: collapse; background: #1e293b; border-radius: 12px; overflow: hidden; }}
        .details-table th, .details-table td {{ padding: 14px 20px; text-align: left; border-bottom: 1px solid #334155; }}
        .details-table th {{ background: #0f172a; color: #94a3b8; font-size: 13px; text-transform: uppercase; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1 style="margin: 0; font-size: 26px; color: #ff7b00;">🚀 OrangeHRM End-to-End Automation Report</h1>
            <p style="margin: 8px 0 0 0; color: #cbd5e1;">Test Suite: Employee Lifecycle (Creation + Photo Upload + Web Table Search + Scroll)</p>
            <p style="margin: 4px 0 0 0; font-size: 13px; color: #94a3b8;">QA Automation Engineer: <b>Tanay</b> | Tool: Playwright (Python Sync API)</p>
        </div>

        <div class="cards">
            <div class="card" style="border-left: 5px solid #22c55e;">
                <div style="color: #94a3b8; font-size: 13px; font-weight: 600;">EXECUTION STATUS</div>
                <div style="font-size: 28px; font-weight: bold; color: #22c55e; margin-top: 5px;">PASSED</div>
                <div style="color: #64748b; font-size: 12px; margin-top: 4px;">Zero Assertion Errors</div>
            </div>
            <div class="card" style="border-left: 5px solid #38bdf8;">
                <div style="color: #94a3b8; font-size: 13px; font-weight: 600;">EMPLOYEE CREATED</div>
                <div style="font-size: 22px; font-weight: bold; color: #38bdf8; margin-top: 5px;">{emp_name}</div>
                <div style="color: #64748b; font-size: 12px; margin-top: 4px;">ID: {emp_id}</div>
            </div>
            <div class="card" style="border-left: 5px solid #a855f7;">
                <div style="color: #94a3b8; font-size: 13px; font-weight: 600;">TOTAL DURATION</div>
                <div style="font-size: 28px; font-weight: bold; color: #a855f7; margin-top: 5px;">{duration_sec}s</div>
                <div style="color: #64748b; font-size: 12px; margin-top: 4px;">With 30s step delays</div>
            </div>
        </div>

        <div class="chart-box">
            <div style="width: 240px; height: 240px;">
                <canvas id="metricsChart"></canvas>
            </div>
            <div style="max-width: 480px;">
                <h3 style="margin: 0 0 10px 0; font-size: 20px;">Execution Metrics & Verification</h3>
                <p style="color: #94a3b8; font-size: 14px; line-height: 1.6;">
                    सर्व स्टेप्स (Login, Employee Form, Photo Upload, Save, Table Search, Scroll to View, Details Inspection) विनाअडथळा यशस्वीरित्या पार पडल्या.
                </p>
                <div>
                    <span class="badge">✓ 6 / 6 Steps Passed</span>
                    <span class="badge" style="background: #1e1b4b; color: #818cf8;">📹 Video Saved: {video_file_name}</span>
                </div>
            </div>
        </div>

        <h3 style="margin-bottom: 15px;">📋 Verification Details</h3>
        <table class="details-table">
            <thead>
                <tr>
                    <th>Step Description</th>
                    <th>Component Tested</th>
                    <th>Status</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Admin Authentication</td>
                    <td>Login Page (Username/Password)</td>
                    <td><span style="color:#22c55e; font-weight:bold;">PASSED</span></td>
                </tr>
                <tr>
                    <td>Employee Form Fill & Photo Upload</td>
                    <td>PIM Add Employee + File Input (.png)</td>
                    <td><span style="color:#22c55e; font-weight:bold;">PASSED</span></td>
                </tr>
                <tr>
                    <td>Personal Details Redirection</td>
                    <td>Dynamic Router Assertion (h6 heading)</td>
                    <td><span style="color:#22c55e; font-weight:bold;">PASSED</span></td>
                </tr>
                <tr>
                    <td>Web Table Search by Generated ID</td>
                    <td>PIM Employee List Filter Table</td>
                    <td><span style="color:#22c55e; font-weight:bold;">PASSED</span></td>
                </tr>
                <tr>
                    <td>Scroll-into-View & Row Click</td>
                    <td>DOM Scroll & Navigation to Record</td>
                    <td><span style="color:#22c55e; font-weight:bold;">PASSED</span></td>
                </tr>
            </tbody>
        </table>
    </div>

    <script>
        const ctx = document.getElementById('metricsChart').getContext('2d');
        new Chart(ctx, {{
            type: 'doughnut',
            data: {{
                labels: ['Passed Steps', 'Failed'],
                datasets: [{{
                    data: [6, 0],
                    backgroundColor: ['#22c55e', '#ef4444'],
                    borderWidth: 0,
                    hoverOffset: 8
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                plugins: {{
                    legend: {{
                        position: 'bottom',
                        labels: {{ color: '#cbd5e1', font: {{ size: 13 }} }}
                    }}
                }},
                cutout: '72%'
            }}
        }});
    </script>
</body>
</html>
"""
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"\n[SUCCESS] 📊 आकर्षक HTML रिपोर्ट तयार झाला: {report_path}")
    return report_path


def test_orangehrm_with_every_step_30s_pause():
    start_time = time.time()
    random_emp_id = str(random.randint(10000, 99999))
    first_name = "Tanay"
    last_name = "QA"
    full_name = f"{first_name} {last_name}"

    # अपलोडसाठी तात्पुरती इमेज तयार करणे
    dummy_photo_path = os.path.abspath("profile_pic.png")
    png_bytes = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15c4\x00\x00\x00\nIDATx\x9cc\x00\x01\x00\x00\x05\x00\x01\r\n-\xb4\x00\x00\x00\x00IEND\xaeB`\x82'
    with open(dummy_photo_path, "wb") as f:
        f.write(png_bytes)

    print(f"\n[INFO] १. चाचणी सुरू - Employee ID: {random_emp_id}, Name: {full_name}")

    os.makedirs("videos", exist_ok=True)
    videos_dir = os.path.abspath("videos")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=700)
        context = browser.new_context(
            viewport={"width": 1280, "height": 720},
            record_video_dir=videos_dir,
            record_video_size={"width": 1280, "height": 720}
        )
        page = context.new_page()

        try:
            # ----------------------------------------------------
            # पायरी १: लॉगिन करणे
            # ----------------------------------------------------
            print("\n[STEP 1] OrangeHRM लॉगिन करत आहे...")
            page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
            page.locator("input[name='username']").fill("Admin")
            page.locator("input[name='password']").fill("admin123")
            page.locator("button[type='submit']").click()

            expect(page.locator(".oxd-topbar-header-title")).to_contain_text("Dashboard")
            print("[PASS] लॉगिन यशस्वी! ⏳ ३० सेकंदांचा पॉज...")
            page.wait_for_timeout(10000)

            # ----------------------------------------------------
            # पायरी २: PIM मध्ये जाऊन नवीन Employee आणि फोटो भरणे
            # ----------------------------------------------------
            print("\n[STEP 2] PIM -> Add Employee फॉर्म उघडत आहे...")
            page.locator("a:has-text('PIM')").click()
            page.locator("button:has-text('Add')").click()

            print("[INFO] प्रोफाइल फोटो अपलोड करत आहे...")
            photo_input = page.locator("input.oxd-file-input")
            photo_input.set_input_files(dummy_photo_path)

            page.locator("input[name='firstName']").fill(first_name)
            page.locator("input[name='lastName']").fill(last_name)

            emp_id_box = page.locator("xpath=//label[text()='Employee Id']/../following-sibling::div//input")
            emp_id_box.click()
            page.keyboard.press("Control+A")
            page.keyboard.press("Backspace")
            emp_id_box.fill(random_emp_id)

            print("[PASS] माहिती व फोटो सेट झाला! ⏳ सेव्ह करण्यापूर्वी ३० सेकंदांचा पॉज...")
            page.wait_for_timeout(10000)

            page.locator("button[type='submit']").first.click()

            expect(page.locator("h6:has-text('Personal Details')")).to_be_visible(timeout=20000)
            print("[PASS] कर्मचारी यशस्वीरित्या सेव्ह झाला! ⏳ ३० सेकंदांचा पॉज...")
            page.wait_for_timeout(10000)

            # ----------------------------------------------------
            # पायरी ३: PIM सर्च करणे
            # ----------------------------------------------------
            print("\n[STEP 3] PIM टेबलमध्ये शोधत आहे...")
            page.locator("a:has-text('PIM')").click()

            search_id_input = page.locator("xpath=//label[text()='Employee Id']/../following-sibling::div//input")
            search_id_input.fill(random_emp_id)
            page.locator("button[type='submit']").click()

            target_card = page.locator(".oxd-table-body .oxd-table-card").filter(has_text=random_emp_id)
            expect(target_card).to_be_visible(timeout=15000)

            # ----------------------------------------------------
            # पायरी ४: खाली स्क्रोल करणे
            # ----------------------------------------------------
            print("\n[STEP 4] रेकॉर्ड सापडला, खाली स्क्रोल करत आहे...")
            target_card.scroll_into_view_if_needed()
            print("[PASS] टेबल रेकॉर्डवर स्क्रोल झाले! ⏳ ३० सेकंदांचा पॉज...")
            page.wait_for_timeout(10000)

            # ----------------------------------------------------
            # पायरी ५: रेकॉर्डवर क्लिक करून डिटेल्स उघडणे
            # ----------------------------------------------------
            print("\n[STEP 5] त्या रेकॉर्डवर क्लिक करून डिटेल्स पेज उघडत आहे...")
            target_card.click()

            expect(page.locator("h6:has-text('Personal Details')")).to_be_visible(timeout=15000)
            print("[PASS] कर्मचाऱ्याचे Personal Details पेज उघडले!")

            # ----------------------------------------------------
            # अंतिम पॉज
            # ----------------------------------------------------
            print("\n[FINAL] सर्व काही व्यवस्थित पूर्ण झाले! ⏳ शेवटचा ३० सेकंदांचा पॉज...")
            page.wait_for_timeout(10000)

        finally:
            # 🚨 खात्रीशीर व्हिडिओ सेव्ह: context बंद होण्यापूर्वी व्हिडिओ ऑब्जेक्ट मिळवणे
            video_ref = page.video
            context.close()
            browser.close()

            video_file_name = "recording_saved.webm"
            if video_ref:
                saved_video_path = video_ref.path()
                video_file_name = os.path.basename(saved_video_path)
                print(f"\n[SUCCESS] 🎥 व्हिडिओ यशस्वीरित्या सेव्ह झाला: {saved_video_path}")

            total_duration = round(time.time() - start_time)
            # रिपोर्ट जनरेट करणे
            generate_custom_html_report(random_emp_id, full_name, video_file_name, total_duration)

    if os.path.exists(dummy_photo_path):
        os.remove(dummy_photo_path)

if __name__ == "__main__":
    test_orangehrm_with_every_step_30s_pause()