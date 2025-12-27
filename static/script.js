// 侧边栏控制
const sidebar = document.getElementById('sidebar');
const toggleSidebar = document.getElementById('toggleSidebar');
const mobileMenuBtn = document.getElementById('mobileMenuBtn');
const body = document.body;

// 切换侧边栏
function toggleSidebarFunc() {
    sidebar.classList.toggle('active');
    body.classList.toggle('sidebar-open');
}

mobileMenuBtn.addEventListener('click', toggleSidebarFunc);
toggleSidebar.addEventListener('click', toggleSidebarFunc);

// 点击侧边栏外部关闭
document.addEventListener('click', (e) => {
    if (sidebar.classList.contains('active') && 
        !sidebar.contains(e.target) && 
        !mobileMenuBtn.contains(e.target)) {
        sidebar.classList.remove('active');
        body.classList.remove('sidebar-open');
    }
});

// 分类折叠功能
const categoryTitles = document.querySelectorAll('.category-title.collapsible');

categoryTitles.forEach(title => {
    title.addEventListener('click', () => {
        const content = title.nextElementSibling;
        title.classList.toggle('collapsed');
        content.classList.toggle('collapsed');
    });
});

// 导航链接高亮和平滑滚动
const navLinks = document.querySelectorAll('.nav-link');

navLinks.forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        const targetId = link.getAttribute('href').substring(1);
        const targetSection = document.getElementById(targetId);
        
        if (targetSection) {
            // 展开目标分类（如果被折叠）
            const categoryTitle = targetSection.querySelector('.category-title');
            const categoryContent = targetSection.querySelector('.category-content');
            if (categoryTitle.classList.contains('collapsed')) {
                categoryTitle.classList.remove('collapsed');
                categoryContent.classList.remove('collapsed');
            }
            
            // 平滑滚动
            targetSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
            
            // 更新导航高亮
            navLinks.forEach(l => l.classList.remove('active'));
            link.classList.add('active');
            
            // 移动端关闭侧边栏
            if (window.innerWidth <= 768) {
                sidebar.classList.remove('active');
                body.classList.remove('sidebar-open');
            }
        }
    });
});

// 滚动时更新导航高亮
let ticking = false;

window.addEventListener('scroll', () => {
    if (!ticking) {
        window.requestAnimationFrame(() => {
            updateActiveNav();
            ticking = false;
        });
        ticking = true;
    }
});

function updateActiveNav() {
    const categorySections = document.querySelectorAll('.category-section');
    const scrollPos = window.scrollY + 100;
    
    categorySections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.offsetHeight;
        const sectionId = section.id;
        
        if (scrollPos >= sectionTop && scrollPos < sectionTop + sectionHeight) {
            navLinks.forEach(link => {
                link.classList.remove('active');
                if (link.getAttribute('href') === `#${sectionId}`) {
                    link.classList.add('active');
                }
            });
        }
    });
}

// 回到顶部按钮
const backToTop = document.getElementById('backToTop');

window.addEventListener('scroll', () => {
    if (window.scrollY > 300) {
        backToTop.classList.add('visible');
    } else {
        backToTop.classList.remove('visible');
    }
});

backToTop.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
});

// 搜索功能
document.getElementById('searchInput').addEventListener('input', function(e) {
    const searchTerm = e.target.value.toLowerCase();
    const projectCards = document.querySelectorAll('.project-card');
    const categorySections = document.querySelectorAll('.category-section');
    
    projectCards.forEach(card => {
        const name = card.getAttribute('data-name');
        const desc = card.getAttribute('data-desc');
        
        if (name.includes(searchTerm) || desc.includes(searchTerm)) {
            card.classList.remove('hidden');
        } else {
            card.classList.add('hidden');
        }
    });
    
    // 隐藏没有可见项目的分类
    categorySections.forEach(section => {
        const visibleCards = section.querySelectorAll('.project-card:not(.hidden)');
        if (visibleCards.length === 0) {
            section.classList.add('hidden');
        } else {
            section.classList.remove('hidden');
            // 搜索时自动展开分类
            const categoryTitle = section.querySelector('.category-title');
            const categoryContent = section.querySelector('.category-content');
            if (searchTerm && categoryTitle.classList.contains('collapsed')) {
                categoryTitle.classList.remove('collapsed');
                categoryContent.classList.remove('collapsed');
            }
        }
    });
});

// 页面加载时自动打开侧边栏（桌面端）
if (window.innerWidth > 768) {
    sidebar.classList.add('active');
    body.classList.add('sidebar-open');
}
