import os
from flask import Flask, render_template_string

app = Flask(__name__)

HTML_CODE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>قريباً | إطلاق برنامج ارتقي التعليمي</title>

<meta name="description" content="قريباً إطلاق برنامج ارتقي التعليمي. تابع العد التنازلي وانضم إلى قناة الواتساب لمعرفة آخر الأخبار والتحديثات.">

<meta name="keywords" content="برنامج ارتقي, تعليم, دورات تعليمية, منصة تعليمية, إطلاق قريب">

<meta name="robots" content="index, follow">

<meta property="og:title" content="قريباً - إطلاق برنامج ارتقي التعليمي">
<meta property="og:description" content="استعدوا لإطلاق برنامج ارتقي التعليمي قريباً.">
<meta property="og:type" content="website">

<style>

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

body {
    background: linear-gradient(135deg, #020617, #1e293b);
    color: white;
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 20px;
}

.container {
    max-width: 620px;
    width: 100%;
    background: rgba(255,255,255,0.06);
    padding: 40px 25px;
    border-radius: 25px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.45);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.15);
}

h1 {
    font-size: 2.3rem;
    margin-bottom: 20px;
    color: #38bdf8;
}

.intro {
    color: #cbd5e1;
    font-size: 1.15rem;
    line-height: 1.8;
    margin-bottom: 35px;
}

.countdown-container {
    display: flex;
    justify-content: center;
    gap: 12px;
    flex-wrap: wrap;
    margin-bottom: 35px;
}

.time-box {
    background: rgba(255,255,255,0.1);
    padding: 15px;
    min-width: 90px;
    border-radius: 15px;
}

.time-box span {
    display: block;
    font-size: 2.2rem;
    font-weight: bold;
}

.time-box label {
    color: #94a3b8;
    font-size: .9rem;
}

.whatsapp-btn {
    display: inline-flex;
    padding: 15px 30px;
    background: #25d366;
    color: white;
    border-radius: 50px;
    text-decoration: none;
    font-weight: bold;
    transition: .3s;
}

.whatsapp-btn:hover {
    transform: translateY(-3px);
}

</style>

</head>

<body>

<div class="container">

<h1>
أهلاً بكم في برنامج ارتقي التعليمي!
</h1>

<p class="intro">
نعمل على إطلاق <strong>برنامج ارتقي التعليمي</strong>.
تابعوا العد التنازلي وانضموا إلى القناة لمعرفة كل جديد.
</p>

<div class="countdown-container">
    <div class="time-box">
        <span id="days">00</span>
        <label>يوم</label>
    </div>
    <div class="time-box">
        <span id="hours">00</span>
        <label>ساعة</label>
    </div>
    <div class="time-box">
        <span id="minutes">00</span>
        <label>دقيقة</label>
    </div>
    <div class="time-box">
        <span id="seconds">00</span>
        <label>ثانية</label>
    </div>
</div>

<div class="whatsapp-section">
<p style="margin-bottom:15px;color:#94a3b8;">
تابعنا على قناة الواتساب للاخبار والدروس:
</p>
<a 
href="https://whatsapp.com/channel/0029VbDH2v5HQbSBDyHL3w2C"
target="_blank"
class="whatsapp-btn">
تابع قناة ارتقي على واتساب
</a>
</div>

</div>

<script>

// تاريخ الإطلاق بتوقيت غزة +03:00
const targetDate = new Date("2026-08-14T00:00:00+03:00").getTime();

function updateCountdown(){
    const now = new Date().getTime();
    const difference = targetDate - now;

    if(difference > 0){
        const days = Math.floor(difference / (1000 * 60 * 60 * 24));
        const hours = Math.floor((difference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((difference % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((difference % (1000 * 60)) / 1000);

        document.getElementById("days").innerHTML = days.toString().padStart(2,'0');
        document.getElementById("hours").innerHTML = hours.toString().padStart(2,'0');
        document.getElementById("minutes").innerHTML = minutes.toString().padStart(2,'0');
        document.getElementById("seconds").innerHTML = seconds.toString().padStart(2,'0');
    }
    else {
        document.querySelector(".container").innerHTML = `
        <h1>
        تم إطلاق برنامج ارتقي التعليمي بنجاح!
        </h1>
        <p class="intro">
        شكرًا لانتظاركم، يمكنكم الآن متابعة المشروع عبر القناة.
        </p>
        `;
    }
}

setInterval(updateCountdown,1000);
updateCountdown();

</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_CODE)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)