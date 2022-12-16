from flask import Flask, render_template, request
from compareJson import get_info
from confGen import generateConfiguration, generateEmail

app = Flask(__name__)







@app.route("/")
def index():
    return render_template("index.html")

##Build sheet output
@app.route("/bsout", methods=['POST', 'GET'])
def buildOutput():
    if request.method == 'POST':
        input = request.form.get('buildOutput')
        #['NET31490-SOGEA-CARTERGATEHOUSE.CE1', 'R', '2033', 'Cisco C927-4P', '', 'PR010667', '/tftpboot/customer-conf/31490', 'Suresh Mogalapu', '', 'Billy Fenton', '', '07/11/2022']
        ##Part code from Input
        f_partcode = input.split("\t")[3]
        
        #All info from Json file
        supplier = get_info(f_partcode)[1]
        ci_name = input.split("\t")[0]
        oper_s = get_info(f_partcode)[0]
        customer_dir = (input.split("\t")[6]).split("/")[-1]

        part_number = get_info(f_partcode)[2]
        print(f"debugging: {part_number}")
        
        #Split from Input
        pick_ref = input.split("\t")[5]
        project_manager = input.split("\t")[9]
        project_eng = input.split("\t")[7]

        
        confOut = generateConfiguration(supplier,ci_name,oper_s,customer_dir)
        emailOut = generateEmail(project_manager,ci_name,supplier,part_number,pick_ref)
        
        
  
        return render_template("buildc.html", confOut=confOut, emailOut=emailOut, ci_name=ci_name, supplier=supplier, oper_s=oper_s, part_number=part_number)



if __name__ == "__name__":
    app.run()