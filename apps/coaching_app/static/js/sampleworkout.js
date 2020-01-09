$(document).ready(function () {
    $("#samplemm").click(function () {
        const $video = $("#video")
        $video.append(`<iframe width="779" height="438" src="https://www.youtube.com/watch?v=fzBgSITMnGo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>`)


        // displaymm()
        // $.get("https://www.youtube.com/embed/qJDpMyUbunw", displaymm)
        // console.log("hello")
        // function displaymm(data) {
        //     console.log("function working")
        //     console.log(data)
        //     showMM(data);
        // }
        // function showMM(data) {
        //     console.log(data)
        //     const $video = $("#video")
        //     $video.append(`<video src="data"></div>`)
        // }
    })
});
