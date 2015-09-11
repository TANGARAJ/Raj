 openerp.newmodule = function (openerp)
{   
openerp.newmoduleMessage.include({

bind_events : function() {
			var self = this;
			this._super.apply(this, arguments);
			this.$('.oe_forward').on('click', this.on_message_forwarded);
		},
on_messages_forward : function(event) {
			event.stopPropagation();
			this.create_thread();
			this.thread.compose_message_forward(event);
			return false;
		},

	});
openerp.newmodule.include({
		compose_message_forward : function(event) {
			event.stopPropagation();
			var action = {
				type : 'ir.actions.act_window',
				res_model : 'wiz',
				view_mode : 'form',
				view_type : 'form',
				views : [ [ false, 'form' ] ],
				target : 'new',
				
			};
			openerp.client.action_manager.do_action(action);
		},

	});
};

