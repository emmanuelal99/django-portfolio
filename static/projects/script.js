// Close the menu when a link is clicked
document.querySelectorAll('.menu-list-items a').forEach(link => {
    link.addEventListener('click', () => {
        const menu = document.querySelector('.menu');
        const hamburger = document.getElementById('hamburger');

        // If the menu is open, close it
        if (menu.classList.contains('active')) {
            menu.classList.remove('active');
            hamburger.classList.remove('active');
        }
    });
});