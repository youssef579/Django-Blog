document.querySelectorAll(".post .menu > i").forEach(function (element) {
    element.onclick = function () {
        let next = element.nextElementSibling
        
        if (getComputedStyle(next).display === "none") {
            next.style.display = "flex";
        } else {
            next.style.display = "none";
        }
    };
});