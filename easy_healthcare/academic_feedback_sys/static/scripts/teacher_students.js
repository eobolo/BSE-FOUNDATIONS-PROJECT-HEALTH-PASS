const allTeacherSpan = document.querySelectorAll(".teacher-span");
console.log(allTeacherSpan);
allTeacherSpan.forEach((element) => {
    element.addEventListener("click", (event) => {
        // get all spans again
        const allTeacherSpanAgain = document.querySelectorAll(".teacher-span");
        // Get the element id to use to get the div to show
        const iconElement = event.target;
        allTeacherSpanAgain.forEach((element) => {
            if (iconElement === element) {
                const iconElementId = iconElement.id;
                const teacherDiv = document.querySelector(`.${iconElementId}`);
                const spanText = iconElement.querySelector('span');
                if (teacherDiv.classList.contains('teacher-display-div2')) {
                    spanText.style.color = "";
                    teacherDiv.classList.remove('teacher-display-div2');
                    teacherDiv.classList.add('teacher-display-div1');
                } else {
                    spanText.style.color = "#268d3e";
                    teacherDiv.classList.remove('teacher-display-div1');
                    teacherDiv.classList.add('teacher-display-div2');
                }
            } else {
                const iconElementId = element.id;
                const teacherDiv = document.querySelector(`.${iconElementId}`);
                teacherDiv.classList.remove('teacher-display-div2');
                teacherDiv.classList.add('teacher-display-div1');
            }
        });
    });
});

const htmlBody = document.querySelector("body");
htmlBody.addEventListener("mouseover", () => {
    const allTeacherSpanAgain = document.querySelectorAll(".teacher-span");
    allTeacherSpanAgain.forEach((element) => {
        const spanText = element.querySelector('span');
        const iconElementId = element.id;
        const teacherDiv = document.querySelector(`.${iconElementId}`);
        teacherDiv.classList.remove('teacher-display-div2');
        teacherDiv.classList.add('teacher-display-div1');
        spanText.style.color = "";
    });
});
// Store the current animation state for all links
const animationStates = new Map();

document.querySelectorAll('.blinking-link').forEach((link) => {
    link.addEventListener('mouseover', (event) => {
        const linkClicked = event.currentTarget;
        // Pause the animation for all links and store their current states
        document.querySelectorAll('.blinking-link').forEach((otherLink) => {
            if (linkClicked !== otherLink) {
                // save the current state of the link not hovered on
                // pause the other links
                const currentState = window.getComputedStyle(otherLink).getPropertyValue('animation-play-state');
                animationStates.set(otherLink, currentState);
                otherLink.style.animationPlayState = 'paused';
            } else {
                // save the current state of the linked overed on
                // which will be the state of the other links
                // now paused the state and add a color to the link
                const currentState = window.getComputedStyle(linkClicked).getPropertyValue('animation-play-state');
                animationStates.set(linkClicked, currentState);
                linkClicked.style.animationPlayState = 'paused';
                linkClicked.style.setProperty("color", "#ee2727", "important");
            }
        });
    });

    link.addEventListener('mouseleave', (event) => {
        // Restore the animation state for all links to their previous states
        document.querySelectorAll('.blinking-link').forEach((allLinks) => {
            const previousState = animationStates.get(allLinks) || 'running';
            allLinks.style.animationPlayState = previousState;
            allLinks.style.color = "";
        });
    });
});