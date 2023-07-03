//cb_handler.js

src="//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"
type=text/javascript
        $(function() {
          checkbox.checked, function(e) {
            e.preventDefault()
            $.getJSON('/send', function(data) {
              //do nothing
            });
            return false;
          }
        });
        


// Get the checkbox element by its id
var checkbox = document.getElementById('myCheckbox');