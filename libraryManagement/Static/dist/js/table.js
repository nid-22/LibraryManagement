$(document).ready(function() {
  
    $('#example2').DataTable({
            pagingType: "full_numbers",
            language: {
            // searchPlaceholder: "Type employee here to search...",search:"",
            info:"_START_ - _END_ of _TOTAL_ ",
            infoEmpty:  " 0 - 0 of 0 ",
            infoFiltered:   " ",
            "lengthMenu": 'Show <select>'+
                       '<option value="10">10 Rows</option>'+
                       '<option value="20">25 Rows</option>'+
                       '<option value="30">50 Rows</option>'+
                       '<option value="40">100 Rows</option>'+
                       '<option value="-1">All Rows</option>'+
                       '</select>',
            oPaginate: {
                      sNext: '<i class="fa fa-angle-right" aria-hidden="true"></i>',
                      sPrevious: '<i class="fa fa-angle-left" aria-hidden="true"></i>',
                      sFirst: '<i class="fa fa-step-backward fa-1x"></i>',
                      sLast: '<i class="fa fa-step-forward fa-1x"></i>',
                      }
                      },
            "paging": true,
            "lengthChange": true, 
            "searching": true,
            "ordering": true,
            "info": true,
            "autoWidth": true,
            'columnDefs': [{
              'orderable': false, // set orderable false for selected columns
            }] ,
          
          orderCellsTop: true,
          "sDom": 'Rfrtlip',
    })
});