(function($){
  $.fn.asDeleteButton = function(){

    $.each(this,function(idx,dom_object){
      var button = $(dom_object);
      var parrent_card = button.closest('div.card');
      button.on('click',function(e){
        e.preventDefault();
        $.ajax({
          url : button.attr('hreff'),
          type : "POST",
          dataType: 'html'
        })
        .fail(function(xhr){
          //deletion failed
          console.log(xhr);
        })
        .done(function(data){
          //deletion complete
        });
        return 0;
      });

    });
  };
}(jQuery));
