// function tplawesome(e, t) {
//     res = e;
//     for (var n = 0; n < t.length; n++) {
//         res = res.replace(/\{\{(.*?)\}\}/g,
//             function (e, r) {
//                 return t[n][r]
//             })
//     }
//     return res
// }

$(function () {
    $("form").on("submit", function (e) {
        e.preventDefault();
        // prepare the request
        console.log(gapi.client.youtube)
        var request = gapi.client.youtube.search.list({
            part: "snippet",
            type: "video",
            q: encodeURIComponent($("#search").val()).replace(/%20/g, "+"),
            maxResults: 1,
            order: "viewCount",
            publishedAfter: "2015-01-01T00:00:00Z"
        });
        // execute the request
        request.execute(function (response) {
            console.log(response)


            const $resultsWrapper = $('#results')
            console.log($resultsWrapper)
            // const $resultsWrapper = $('<div> hello again</div>')

{/* <iframe class="video" width="640" height="360" src="//www.youtube.com/embed/{{videoid}}" frameborder="0" allowfullscreen></iframe> */}

            $resultsWrapper.append(`<h3>${response.result}</h3>`)
            console.log(response.result.items[0].id.videoId)
            // var itemid = response.result.items[0].id.videoId
            // var videoid = 
            $resultsWrapper.append(`<iframe class="video" width="640" height="360" src="http://www.youtube.com/embed/${response.result.items[0].id.videoId}" frameborder="0" allowfullscreen></iframe>`)



            // var results = response.result;
            // $.each(results.items, function (index, item) {
            //     console.log(item)
            //     console.log(item.snippet.title)
            //     $.get("/item", function (data) {
            //         $("#results").append(tplawesome(data, [{ "title": item.snippet.title, "videoid": item.id.videoId }]));
            //     });
            // });
        });
    });
});



function init() {
    gapi.client.setApiKey("AIzaSyCVuN7GOKmyHIT0xtpd2WTM4n9pEI-zwXQ");
    gapi.client.load("youtube", "v3", function () {
        // yt api is ready
    });
}