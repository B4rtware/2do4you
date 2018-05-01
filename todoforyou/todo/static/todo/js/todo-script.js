$(document).ready(function () {
    var descriptions = [
        "Hitmarker indicator is reversed on client or server",
        "Basic HUD (Improvements)",
        "If the player changes the weapon within the ingame menu the Players orientation gets resets to the middle",
        "Without default maps selected you cant host a game",
        "Weapon Different Clip / Ammo Sizes",
        "Emblems to equip and displayed on the character card",
        "Enemy can't damage Main Character (Host)"];
    var deadlines = [
        "13.09.2019",
        "14.10.2018",
        "29.07.2018",
        "29.03.2018",
        "01.12.2018",
        "11.06.2018",
        "29.01.2018"];
    var progresses = [
        "79",
        "10",
        "39",
        "100",
        "11",
        "83",
        "100"]

    $.each(descriptions, function(index, value) {
        var card = $("#initial-card").clone()
        /* remove the "initial-card" id which is only beeing used for the first card */
        card[0].removeAttribute("id");
        /* set the todo description */
        card.find("div:first-child > p:first-child").text(value)
        /* set the deadline */
        card.find("div:first-child > div > div:nth-child(2) > u").text(deadlines[index])
        /* set the current todo progress */
        var progressbar = card.find("div:first-child > div:nth-child(3) > div > div")
        progressbar.text(progresses[index] + "%");
        progressbar.css("width", progresses[index] + "%");
        progressbar.attr("aria-valuenow", progresses[index]);

        /* append the modified card to the columns layout */
        card.appendTo(".card-columns");
    })    
});