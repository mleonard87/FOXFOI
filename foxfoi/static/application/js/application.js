function setActiveCaseSection(activeSection) {
    $("#case-sub-nav").find("dd").removeClass("active");
    $("#case-sub-nav").find("dd[name = '" + activeSection + "']").addClass("active");
}

$(document).ready(function() {
    setActiveCaseSection($("#active_page").val());

    $(".keyterm-status").on("click", function() {
        $(this).parents(".keyterm-change-status-form").submit();
    });

    $(".complete-referral-form").on("click", function() {
        $(this).submit();
    });
});
