openerp.checking = function(openerp) {
      openerp.web.form.widget.add('test','openerp.web.form.test');


    openerp.web.form.test = openerp.web.form.FieldChar.extend(
    {    
       template: 'test_button',

       init: function () {
                 this._super.apply(this, arguments);
                 this._start = null;
                 console.log('INIT');

       },

       start: function() {
             console.log('START');   
             $('button#bstart').click(this.myfunction);  //link button to function  
        },

        myfunction: function() {
              //DO WHAT YOU WANT
        }
...
