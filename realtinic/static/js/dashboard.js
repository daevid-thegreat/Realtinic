$(".dashboard-menu-btn").on("click", function () {
    $(".dashbard-menu-wrap").addClass("dashbard-menu-wrap_vis");
    $(".dashbard-menu-overlay").fadeIn(100);
});
$(".dashbard-menu-close , .dashbard-menu-overlay").on("click", function () {

    $(".dashbard-menu-wrap").removeClass("dashbard-menu-wrap_vis");
    $(".dashbard-menu-overlay").fadeOut(100);
});

//   css ------------------
var $window2 = $(window);

$window2.on("resize", function () {

    var ww3 = $window2.width();
    if (ww3 > 1270) {
        $(".dashbard-menu-overlay").css({
            display: "none"
        });
        $(".dashbard-menu-wrap").removeClass("dashbard-menu-wrap_vis");
    }

});





const ul = document.querySelector("ul[name=features-ul]"),
input = document.querySelector("input[name=features]"),
tagNumb = document.querySelector(".tag-details span");

let maxTags = 16,
tags = ["coding"];
var features = {"input[name=features]" : tags}

countTags();
createTag();

function countTags(){
    input.focus();
    tagNumb.innerText = maxTags - tags.length;
}

function createTag(){
    ul.querySelectorAll("li").forEach(li => li.remove());
    tags.slice().reverse().forEach(tag =>{
        let liTag = `<li>${tag} <i class="uit uit-multiply" onclick="remove(this, '${tag}')"></i></li>`;
        ul.insertAdjacentHTML("afterbegin", liTag);
    });
    countTags();
}

function remove(element, tag){
    let index  = tags.indexOf(tag);
    tags = [...tags.slice(0, index), ...tags.slice(index + 1)];
    element.parentElement.remove();
    countTags();
}

function addTag(e){
    if(e.key == "Enter"){
        let tag = e.target.value.replace(/\s+/g, ' ');
        if(tag.length > 1 && !tags.includes(tag)){
            if(tags.length < 16){
                tag.split(',').forEach(tag => {
                    tags.push(tag);
                    createTag();
                });
            }
        }
        e.target.value = "";
    }
}

input.addEventListener("keyup", addTag);

const removeBtn = document.querySelector(".tag-details button");
removeBtn.addEventListener("click", () =>{
    tags.length = 0;
    ul.querySelectorAll("li").forEach(li => li.remove());
    countTags();
});

$(document).ready(function() {
    $(window).keydown(function(event){
      if(event.keyCode == 13) {
        event.preventDefault();
        return false;
      }
    });
  });