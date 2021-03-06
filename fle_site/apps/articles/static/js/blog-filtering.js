$(function() {
    // onload, update # of total posts 
    updatePostNumbers();

    // Filter by tag
    $('#tag-filters button').click(function() {
        // Highlight the tag cloud and any other posts
        $(this).toggleClass("active");
        animateExplicitly($(this), false);
        $('button[data-id="post-tag-' + $(this).attr("data-id") + '"]').removeClass("btn-default").addClass("btn-primary");
        filterPosts();
    });

    // Remove filters 
    $(document).on(
        'click',
        '#filtering-header button.remove-tag-container',
        function() {
            var tagSlug = $(this).attr('data-id');
            var filterElement = $('#tag-filters button[data-id="' + tagSlug + '"]');
            filterElement.toggleClass("active");
            animateExplicitly(filterElement, true);
            $('button[data-id="post-tag-' + tagSlug + '"]').removeClass("btn-primary").addClass("btn-default");
            animateExplicitly($(this), false);
            filterPosts();
        }
    );

    // Clear all  
    $(document).on('click', '.clear-all-filters', resetFilters);

    // Expand & contract months
    $('.month-expand').click(function(ev) {
        ev.preventDefault();
        $(this).toggleClass('dropup');
        var postList = $(this).next('ul');
        postList.slideToggle("fast");
    });
});

function filterPosts() {
    // filter posts once we update active filters

    var activeFilters = getFiltersByStatus(true);
    var activeFilterSlugs = getFilterProperties(activeFilters, "slug");
    var activeFilterNames = getFilterProperties(activeFilters, "name");

    // Show & hide the posts that match the tag sets
    var posts = $('li[id^="post-"]');
    var totalPosts = posts.length;
    var postsShowing = 0;

    posts.each(function() {
        // Create list of the post's tags
        var postTags = $(this).attr("data-id").split(/[ ]+/);
        // show the post if all of it's tags match the activeFilter tag slugs
        if (_.difference(activeFilterSlugs, postTags).length === 0) {
            animateExplicitly($(this), true);
            postsShowing = postsShowing + 1;
        } else {
            animateExplicitly($(this), false);
        }
    });

    // Update HTML to show we are filtering based on tags
    if (activeFilterSlugs.length > 0) {
        var filterTags = "<h2>Tags:</h2> ";
        for (var i = 0; i < activeFilterSlugs.length; i++) {
            filterTags += "<button class='btn btn-md btn-default tag-bubble remove-tag-container' data-id='" + activeFilterSlugs[i] + "'>" + activeFilterNames[i] + "<a href='#' class='remove-filter'>x</a></button>";
        };
        filterTags += "<a href='' class='clear-all-filters'>Clear All</a>";
        $('#post-numbers a.clear-all-filters').show('fast');
        $('#filtering-header').html(filterTags);
    } else {
        $('#filtering-header').html("<h2>All Posts</h2>");
        $('.clear-all-filters').hide();
    }

    updatePostNumbers();
    smartFilterDisabling();
}

function resetFilters(ev) {
    ev.preventDefault();
    // Show all posts & reset highlights
    var posts = $('li[id^="post-"');
    posts.each(function() {
        var buttons = $(this).find('button.tag-bubble');
        buttons.removeClass("btn-primary").addClass("btn-default");
        animateExplicitly($(this), true);
    });
    // Show all filters
    $('#tag-filters').children('button').each(function() {
        $(this).removeClass("active");
        animateExplicitly($(this), true);
    });
    // Hide all tags
    animateExplicitly($('#filtering-header').children('button'), false);

    $('#filtering-header').html("<h2>All Posts</h2>");
    $('.clear-all-filters').hide('fast');

    updatePostNumbers();
    smartFilterDisabling();
}

function getFiltersByStatus(active) {
    // Return a list of active or inactive filter slugs, and a list of filter names
    // get active tag slugs & names 
    var tagObjects = [];
    if (active) {
        var tagFilter = $('#tag-filters button.active');
    } else {
        var tagFilter = $('#tag-filters button:not(.active)');
    }
    tagFilter.each(function() {
        tagObjects.push($(this));
    });
    return tagObjects;
}

function getFilterProperties(filters, property) {
    // Return list of all filter properties (either names or slugs)
    var filterProps = [];
    if (property === "slug") {
        var filterProps = $.map(filters, function(element) {
            return element.attr("data-id")
        });
    } else if (property === "name") {
        var filterProps = $.map(filters, function(element) {
            return element.text()
        });
    }
    return filterProps;
}

function updatePostNumbers() {
    var totalPosts = $('li[id^="post-"');
    var postsShowing = totalPosts.filter(':visible');
    $('#posts-showing').html(postsShowing.length);
    $('#total-posts').html(totalPosts.length);
}

function smartFilterDisabling() {
    // Disable filters that would lead to 0 posts displaying
    // when combined with currently active filters
    var inactiveFilters = getFiltersByStatus(false);

    // For each one, check if it is a tag of any current post
    var posts = $('#post-list li[id^="post-"').filter(function() {
        var element = $(this);
        if (element.attr("data-visible") === "false") {
            return false;
        }
        return true;
    });

    var allPostTags = []
    posts.each(function() {
        var postTags = $(this).attr("data-id").split(/[ ]+/);
        allPostTags = _.uniq(allPostTags.concat(postTags));
    });

    for (var i = 0; i < inactiveFilters.length; i++) {
        if (allPostTags.indexOf(inactiveFilters[i].attr("data-id")) >= 0) {
            inactiveFilters[i].prop("disabled", false);
        } else {
            inactiveFilters[i].prop("disabled", true);
        }
    };
}

function animateExplicitly(element, visibility) {
    // Call jQuery show/hide method after adding an attribute to 
    // indicate visibility (so we can check for it later in the code)
    element.attr("data-visible", visibility);
    element.toggle(visibility);
}