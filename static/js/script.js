$(document).ready(function(){
    $(".dropdown-trigger").dropdown({
        coverTrigger: false
    });
    $('.sidenav').sidenav();
    $('.collapsible').collapsible();
    $('.fixed-action-btn').floatingActionButton({
      direction: 'top',
      hoverEnabled: true
    });
    $('.modal').modal();
    $('select').formSelect({
      isMultiple: true
    });
    $('.tooltipped').tooltip();
    $('.scroll-up').on('click', function() {
        $('html, body').animate({scrollTop:0}, '300');
    });
    $('#search').click(function() {
        $('.search-panel').show("slow");
    });
    $('.search').on('click', function() {
        $('html, body').animate({scrollTop:0}, '300')
        $('.search-panel').show("slow");
    });
    /*Detect scroll to the bottom sourced from https://gist.github.com/toshimaru/6102647 */
    $(window).on("scroll", function() {
        var scrollHeight = $(document).height();
        var scrollPosition = $(window).innerHeight() + $(window).scrollTop();
        if ((scrollHeight - scrollPosition) < 1) {
            $('#FAB').css('background-color', 'white')
            $('.fa-bars').css('color', 'black')
        } else {
            $('#FAB').css('background-color', 'black')
            $('.fa-bars').css('color', 'white')
        }
    });
    /* Disable hoverEnabled option on floating action button for mobile & tablet viewports */
    if (window.matchMedia("(max-width: 600px)").matches) {
        $('.fixed-action-btn').floatingActionButton({
            hoverEnabled: false
        })
    }

    /* The code below is the CI solution for the Materialize select box validation issue taken from the 
    'Task manager' mini-project:
    https://github.com/Code-Institute-Solutions/TaskManagerAuth/blob/main/
    04-AddingATask-WritingToTheDatabase/02-materialize-select-validation/static/js/script.js
    */
    validateMaterializeSelect();
    function validateMaterializeSelect() {
        let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
        let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
        if ($("select.validate").prop("required")) {
            $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
        }
        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            $(this).parent(".select-wrapper").on("change", function () {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function () {
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {
                $(".select-wrapper input.select-dropdown").on("focusout", function () {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
        });
    }
});



       