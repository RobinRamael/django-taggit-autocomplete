$(document).ready(function() {
    function split( val ) {
	return val.split( /,\s*/ );
    }
    function extractLast( term ) {
	return split( term ).pop();
    }
    $( "#%s" )
    // don't navigate away from the field on tab when selecting an item
	.bind( "keydown", function( event ) {
	    if ( event.keyCode === $.ui.keyCode.TAB &&
		 $( this ).data( "ui-autocomplete" ).menu.active ) {
		event.preventDefault();
	    }
	})
	.autocomplete({
	    minLength: 0,
	    source: function(request, response) {
		var url = "%s" + "?term=" + extractLast(request.term)
		console.debug(url)
		$.getJSON(url,
			  function(data) {
			      console.debug(data)
			      response(data)
			  });
	    },
	    focus: function() {
		// prevent value inserted on focus
		return false;
	    },
	    select: function( event, ui ) {
		var terms = split( this.value );
		// remove the current input
		terms.pop();
		// add the selected item
		terms.push( ui.item.value );
		// add placeholder to get the comma-and-space at the end
		terms.push( "" );
		this.value = terms.join( ", " );
		return false;
	    }
	});
});
