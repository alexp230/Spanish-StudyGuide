# from flask import Flask, render_template, request
# import Study




# app = Flask(__name__)

# @app.route("/", methods=['GET', 'POST'])
# def home():
#     select_options = []
    
#     if (request.method == 'POST'):

#         select_options = request.form.getlist('options')

#         if ((len(select_options)) != 0):

#             Study.Startup(select_options)

#             print(select_options)

#     return render_template("index.html")

# if __name__ == "__main__":
#     app.run()