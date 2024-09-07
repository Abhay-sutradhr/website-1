$(document).ready(function() {
    // Switch to list view
    $('#list').click(function(event) {
        event.preventDefault();
        $('#products .item').addClass('list-group-item');
        $('#products .item').removeClass('grid-group-item');
    });
    
    // Switch to grid view
    $('#grid').click(function(event) {
        event.preventDefault();
        $('#products .item').removeClass('list-group-item');
        $('#products .item').addClass('grid-group-item');
    });
});