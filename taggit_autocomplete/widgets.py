from django import forms
from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils.safestring import mark_safe

from utils import edit_string_for_tags

from os import path




SCRIPT = """<script>
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
</script>
"""

class TagAutocomplete(forms.TextInput):
	input_type = 'text'

	def render(self, name, value, attrs=None):
		list_view = reverse('taggit_autocomplete-list')
		if value is not None and not isinstance(value, basestring):
			value = edit_string_for_tags([o.tag for o in value.select_related("tag")])
		html = super(TagAutocomplete, self).render(name, value, attrs)
		js = SCRIPT % (attrs['id'], list_view)
		return mark_safe("\n".join([html, js]))
