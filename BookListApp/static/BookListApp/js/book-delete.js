(function($){
  var _delete_object;
  var _link;
  var _deleteRequest = function(href, entry){
    $.ajax({
      url : href,
      type : "POST",
      dataType: 'html'
    })
    .fail(function(xhr){
      //deletion failed
      console.log(xhr);
    })
    .done(function(data){
      //deletion complete
      entry.fadeOut();
    });//end of ajax req
  };



  $.fn.asDeleteButton = function(){
    $.each(this,function(idx,dom_object){
      $(dom_object).on('click',function(e){
        e.preventDefault();
        _link = $(dom_object).attr('href');
        _delete_object = $(dom_object).closest('div.card');
      });//end delete link event
    });//end each
    return this;
  };

  $.fn.asConfirmModal = function(){
    $.each(this, function(idx, dom_object){
      $(dom_object).on('shown.bs.modal', function(e){
        $(this).find('#btn-cancel-delete');
        $(this).find('.btn-ok').on('click', function(e){
          _deleteRequest(_link, _delete_object);
        }).focus();
      });
    });
    return this;
  };
}(jQuery));
