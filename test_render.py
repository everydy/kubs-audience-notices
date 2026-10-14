import subprocess

html_content = """<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css">
  <style>
    @page { size: A4 landscape; margin: 0; }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: 'Pretendard', sans-serif; }
    .sheet {
      width: 297mm; height: 210mm; padding: 9mm 11mm;
      display: flex; flex-direction: column; justify-content: space-between;
    }
    .outer-frame {
      width: 100%; height: 100%; border: 5px solid #b91c1c; border-radius: 14px;
      padding: 8mm 13mm; display: flex; flex-direction: column; justify-content: space-between;
    }
    .notice-header { display: flex; justify-content: center; border-bottom: 2.5px solid #e5e7eb; padding-bottom: 3.5mm; }
    .badge-tag {
      padding: 6px 18px; border-radius: 9999px; font-size: 15pt; font-weight: 900;
      background-color: #fef2f2; color: #b91c1c; border: 2.5px solid #dc2626;
    }
    .notice-body { flex: 1; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; }
    .lead-phrase { font-size: 32pt; font-weight: 800; color: #374151; margin-bottom: 4mm; }
    .core-phrase { font-weight: 900; letter-spacing: -0.04em; color: #dc2626; margin-bottom: 5mm; white-space: nowrap; }
    .underline-mark { background: linear-gradient(to top, #fee2e2 42%, transparent 42%); padding: 0 8px; }
    .callout-box {
      width: fit-content; max-width: 200mm; border-radius: 10px; padding: 4mm 14mm;
      display: inline-flex; align-items: center; gap: 12px;
      background-color: #fef2f2; border: 3.5px solid #dc2626; color: #991b1b;
    }
    .notice-footer { display: flex; justify-content: space-between; border-top: 2.5px solid #e5e7eb; padding-top: 3mm; font-size: 12.5pt; font-weight: 700; color: #4b5563; }
  </style>
</head>
<body>
  <div class="sheet">
    <div class="outer-frame">
      <div class="notice-header">
        <div class="badge-tag">🚫 방송 중계 구역</div>
      </div>
      <div class="notice-body">
        <div class="lead-phrase">중계로 인해 해당 좌석 대신</div>
        <div class="core-phrase" style="font-size: 68pt;">
          <span class="underline-mark">다른 자리 이용 부탁드립니다.</span>
        </div>
        <div class="callout-box">
          <span style="font-size: 28pt;">🎥</span>
          <span style="font-size: 24pt; font-weight: 900;">중계 장비 운용 좌석으로 착석이 불가합니다.</span>
        </div>
      </div>
      <div class="notice-footer">
        <div>※ 원활한 생중계 방송을 위한 조치이오니 관람객 여러분의 양해를 부탁드립니다.</div>
        <div style="font-weight: 900; color: #111;">고려대학교 교육방송국 KUBS</div>
      </div>
    </div>
  </div>
</body>
</html>
"""

with open("test_icehockey.html", "w", encoding="utf-8") as f:
    f.write(html_content)

subprocess.run([
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
    "--print-to-pdf=test_icehockey.pdf", "file:///Users/moonsoo/projects/audience_notices_a4/test_icehockey.html"
], check=True)

subprocess.run([
    "qlmanage", "-t", "-s", "2400", "-o", ".", "test_icehockey.pdf"
], check=True)

print("Done test render")
