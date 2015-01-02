function setActiveCaseSection(activeSection) {
    $("#case-sub-nav").find("dd").removeClass("active");
    $("#case-sub-nav").find("dd[name = '" + activeSection + "']").addClass("active");
}

$(document).ready(function() {
    setActiveCaseSection($("#active_page").val());
});
