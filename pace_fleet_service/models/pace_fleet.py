# from odoo import api, models, _
# import urllib

# class FleetVehicle(models.Model):
    # _inherit = "fleet.vehicle"


    # @api.model
    # def create(self, vals):
        # res = super(FleetVehicle, self).create(vals)
        # if res.x_studio_odometer_to_service < 1000:
          # if res.x_studio_service_request_sms_sent == False:
            # if res.x_studio_next_service_scheduled == False:
                # headers = {"Content-Type": "application/json", "Accept": "application/json", "Catch-Control": "no-cache"}
                # #full_url = "https://api.smsportal.com/api5/http5.aspx?Type=sendparam&username=Pacecar&password=3414street&numto=%s&data1=%s" % (res.driver_id.mobile.replace(" ",""), 'Hi%20' + res.driver_id.name.replace(" ", '%20') + '%20Your%20vehicle%20' + self.license_plate + '%20is%20now%20due%20for%20service.%20Book%20your%20service%20online%20now.%20PACE%20FLEET')
                # full_url = "http://www.mymobileapi.com/api5/http5.aspx?Type=sendparam&username=Pacecar&password=3414street&numto=%s&data1=%s" % (res.driver_id.mobile.replace(" ",""), 'Hi%20' + res.driver_id.name.replace(" ", '%20') + '%20Your%20vehicle%20' + self.license_plate + '%20is%20now%20due%20for%20service.%20Click%20this%20link%20to%20book%20now%20https://pace-fleet-services.odoo.com/calendar/service-appointments-1/appointment%20,%20PACE%20FLEET.')
                # req = urllib.request.Request(full_url, headers=headers)
                # details_data = urllib.request.urlopen(req)
                # details_data = details_data.read()
                
                # res.x_studio_service_request_sms_sent = 1
            # return res


    # def write(self, vals):
        # super(FleetVehicle, self).write(vals)
        # if self.x_studio_odometer_to_service < 1000:
          # if self.x_studio_service_request_sms_sent == False:
            # if self.x_studio_next_service_scheduled == False:     
                # headers = {"Content-Type": "application/json", "Accept": "application/json", "Catch-Control": "no-cache"}
                # #full_url = "https://api.smsportal.com/api5/http5.aspx?Type=sendparam&username=Pacecar&password=3414street&numto=%s&data1=%s" %(self.driver_id.mobile.replace(" ",""), 'Hi%20' + self.driver_id.name.replace(" ", '%20') + '%20Your%20vehicle%20' + self.license_plate + '%20is%20now%20due%20for%20service.%20Book%20your%20service%20online%20now.%20PACE%20FLEET')
                # full_url = "http://www.mymobileapi.com/api5/http5.aspx?Type=sendparam&username=Pacecar&password=3414street&numto=%s&data1=%s" %(self.driver_id.mobile.replace(" ",""), 'Hi%20' + self.driver_id.name.replace(" ", '%20') + '%20Your%20vehicle%20' + self.license_plate + '%20is%20now%20due%20for%20service.%20Click%20this%20link%20to%20book%20now%20https://pace-fleet-services.odoo.com/calendar/service-appointments-1/appointment%20,%20PACE%20FLEET.')
                # req = urllib.request.Request(full_url, headers=headers)
                # details_data = urllib.request.urlopen(req)
                # details_data = details_data.read()
                
                # self.x_studio_service_request_sms_sent = 1

