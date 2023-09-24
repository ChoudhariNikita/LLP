/*!
    * Start Bootstrap - SB Admin v7.0.7 (https://startbootstrap.com/template/sb-admin)
    * Copyright 2013-2023 Start Bootstrap
    * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-sb-admin/blob/master/LICENSE)
    */
    // 
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    // Toggle the side navigation
    const sidebarToggle = document.body.querySelector('#sidebarToggle');
    if (sidebarToggle) {
        // Uncomment Below to persist sidebar toggle between refreshes
        // if (localStorage.getItem('sb|sidebar-toggle') === 'true') {
        //     document.body.classList.toggle('sb-sidenav-toggled');
        // }
        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            document.body.classList.toggle('sb-sidenav-toggled');
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
        });
    }

});


// -------------
 // JavaScript logic to dynamically generate course cards based on user progress
        // For this example, we assume the user's completed courses are stored in an array
        const completedCourses = [
            {
                title: "Course 1",
                progress: 100, // Progress in percentage
            },
            {
                title: "Course 2",
                progress: 75,
            },
            // Add more completed courses as needed
        ];

        const courseList = document.getElementById("course-list");
    // Iterate through completed courses and generate course cards
    completedCourses.forEach((course) => {
            const courseCard = document.createElement("div");
            courseCard.classList.add("course-card");

            const courseTitle = document.createElement("h2");
            courseTitle.classList.add("course-title");
            courseTitle.innerText = course.title;

            const courseProgress = document.createElement("p");
            courseProgress.classList.add("course-progress");
            courseProgress.innerText = `Progress: ${course.progress}%`;

            courseCard.appendChild(courseTitle);
            courseCard.appendChild(courseProgress);

            courseList.appendChild(courseCard);
        });

// ---------------
// JavaScript logic to dynamically generate achievement cards based on user progress
        // Retrieve user achievements from the server and populate the section
        // You may use AJAX or the fetch API to fetch achievement data from the server
        // Example data structure:
        const achievementsData = [
            {
                name: "Course Completion",
                badge: "✔️",
                description: "Completed the Beginner Course",
            },
            {
                name: "Module Completion",
                badge: "🏆",
                description: "Mastered Module 1: Vocabulary",
            },
            // Add more achievement objects as needed
        ];
        const achievementsSection = document.querySelector(".achievements");

        achievementsData.forEach((achievement) => {
            const achievementCard = document.createElement("div");
            achievementCard.classList.add("achievement-card");

            const badge = document.createElement("div");
            badge.classList.add("achievement-badge");
            badge.innerText = achievement.badge;

            const name = document.createElement("h3");
            name.innerText = achievement.name;

            const description = document.createElement("p");
            description.innerText = achievement.description;

            achievementCard.appendChild(badge);
            achievementCard.appendChild(name);
            achievementCard.appendChild(description);

            achievementsSection.appendChild(achievementCard);
        });

    // -----------------