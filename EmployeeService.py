#
# The original code for this example is credited to S. Subramanian,
# from this post on DZone: https://dzone.com/articles/restful-web-services-with-python-flask
#

from flask import Flask
from flask import jsonify
from flask import request
from flask import abort

app = Flask(__name__)

empDB=[
 {
 'id':'101',
 'name':'Saravanan S',
 'title':'Technical Leader',
 'salary':'500'
 },
 {
 'id':'201',
 'name':'Rajkumar P',
 'title':'Sr Software Engineer',
 'salary': '50000'
 }
 ]

@app.route('/empdb/employee',methods=['GET'])
def getAllEmp():
    return jsonify({'emps':empDB})

@app.route('/empdb/employee/<empId>',methods=['GET'])
def getEmp(empId):
    for emp in empDB:
        if(emp['id'] == empId):
            usr = emp;
            return jsonify({'emp':usr})
        else:
            usr = jsonify({'message':"id not found.",
                    'category':"error",
                    'status':404})
    return usr
    # usr = [ emp for emp in empDB if (emp['id'] == empId) ] 
    


@app.route('/empdb/employee/<empId>',methods=['PUT'])
def updateEmp(empId):

    em = [ emp for emp in empDB if (emp['id'] == empId) ]

    if len(em) > 0:
        if 'name' in request.json : 
            em[0]['name'] = request.json['name']

        if 'title' in request.json:
            em[0]['title'] = request.json['title']
        
        if 'salary' in request.json:
            em[0]['salary'] = request.json['salary']
    
    else:
        em = jsonify({'message':"id not found.",
                    'category':"error",
                    'status':404})

    return jsonify(em)

@app.route('/empdb/employee/<empId>/<empSal>',methods=['PUT'])
def updateEmpSal(empId, empSal):

    em = [ emp for emp in empDB if (emp['id'] == empId) ]

    if len(em) > 0:
        em[0]['salary'] = empSal;
    else:
        em = jsonify({'message':"id not found.",
                    'category':"error",
                    'status':404})

    return jsonify(em)


@app.route('/empdb/employee',methods=['POST'])
def createEmp():

    dat = {
    'id':request.json['id'],
    'name':request.json['name'],
    'title':request.json['title'],
    'salary':request.json['salary']
    }
    empDB.append(dat)
    return jsonify(dat)

@app.route('/empdb/employee/<empId>',methods=['DELETE'])
def deleteEmp(empId):
    em = [ emp for emp in empDB if (emp['id'] == empId) ]

    if len(em) > 0:
        empDB.remove(em[0])
        return jsonify({'response':'Success'})
    else:
        return jsonify({'response':'Failure'})

if __name__ == '__main__':
 app.run(host='0.0.0.0', port=5000)
