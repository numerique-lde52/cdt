// target='_blank' on url that are not par of the current domain
// or for internals pdf documents
// see http://stackoverflow.com/questions/4425198/markdown-target-blank
(function() {
    var links = document.links;
    for (var i = 0, linksLength = links.length; i < linksLength; i++) {

        l = links[i];

        var is_external_link = l.hostname != window.location.hostname;
        var is_internal_document = is_external_link == false && l.pathname.includes("assets") && l.pathname.includes(".pdf");


       if (is_external_link || is_internal_document) {
           links[i].target = '_blank';
           links[i].className += ' externalLink'
       }
    }
})();
