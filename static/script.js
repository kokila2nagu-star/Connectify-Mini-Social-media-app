// Like button animation

document.addEventListener("DOMContentLoaded", function(){

    const likeButtons = document.querySelectorAll(".like");


    likeButtons.forEach(button => {

        button.addEventListener("click", function(){

            this.innerHTML = "❤️ Liked";

            this.style.transform = "scale(1.1)";


            setTimeout(() => {

                this.style.transform = "scale(1)";

            },200);

        });

    });



    // Confirm logout

    const logoutLink = document.querySelector(".logout-link");


    if(logoutLink){

        logoutLink.addEventListener("click", function(event){

            let confirmLogout = confirm(
                "Are you sure you want to logout?"
            );


            if(!confirmLogout){

                event.preventDefault();

            }

        });

    }



    // Search animation

    const searchBox = document.querySelector(".search input");


    if(searchBox){

        searchBox.addEventListener("focus",function(){

            this.style.border = "2px solid gold";

        });



        searchBox.addEventListener("blur",function(){

            this.style.border = "1px solid #7c3aed";

        });

    }



    // Post creation message

    const postButton = document.querySelector(".create button");


    if(postButton){

        postButton.addEventListener("click",function(){

            this.innerHTML="Posting... 🚀";

        });

    }


});