document.addEventListener('DOMContentLoaded', () => {
    const banner = document.getElementById('cookie-banner');
    const acceptBtn = document.getElementById('accept-btn');

    // 1. 检查浏览器本地存储：是否已经存过 'cookieAccepted'
    const hasAccepted = localStorage.getItem('cookieAccepted');

    // 2. 如果没点过接受，就显示横幅（移除 hidden 类）
    if (!hasAccepted) {
        banner.classList.remove('hidden');
    }

    // 3. 监听点击事件
    acceptBtn.addEventListener('click', () => {
        // 在本地存储存入一个标记，告诉浏览器“用户同意了”
        localStorage.setItem('cookieAccepted', 'true');
        
        // 隐藏横幅
        banner.classList.add('hidden');
    });
});