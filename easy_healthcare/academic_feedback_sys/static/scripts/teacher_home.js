const callback = (entries, observer) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting) {
            let currentSection = entry.target;
            // console.log(currentSection);
            currentSection = currentSection.querySelector('.section-div')
            if (currentSection.classList.contains("even-div")) {
                currentSection.classList.remove("div-display2");
                currentSection.classList.remove("even-div-animation-reverse");
                currentSection.classList.add("even-div-animation");
                console.log("intersection even is working");
            } else {
                currentSection.classList.remove("div-display1");
                currentSection.classList.remove("odd-div-animation-reverse");
                currentSection.classList.add("odd-div-animation");
                console.log("intersection odd is working");
            }
        } else {
            let currentSection = entry.target;
            // console.log(currentSection);
            currentSection = currentSection.querySelector('.section-div');
            if (currentSection.classList.contains("odd-div")) {
                if (currentSection.classList.contains("div-display1")) {
                } else {
                    currentSection.classList.remove("odd-div-animation");
                    currentSection.classList.add("odd-div-animation-reverse");
                    currentSection.classList.add("div-display1");
                }
            } else {
                if (currentSection.classList.contains("div-display2")) {
                } else {
                    currentSection.classList.remove("even-div-animation");
                    currentSection.classList.add("even-div-animation-reverse");
                    currentSection.classList.add("div-display2");
                }               
            }         
        }
    });
}
let options = {
    root: null,
    rootMargin: "0px",
    threshold: 0.5,
}

const observer = new IntersectionObserver(callback, options);
const targets = document.querySelectorAll(".sections");
targets.forEach((eachTarget) => observer.observe(eachTarget));