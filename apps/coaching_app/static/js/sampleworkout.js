$(document).ready(function () {
    $("#samplemm").click(function () {
        const $video = $("#video")
        $video.append(`<iframe width="710" height="397" src="https://www.youtube.com/embed/fzBgSITMnGo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>`)
    })
});