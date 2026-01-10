from datetime import datetime
from flask import Blueprint
from flask import render_template, flash, redirect, url_for, request



from config import Config

routes_blueprint = Blueprint("routes", __name__)
routes_blueprint.template_folder = Config.TEMPLATE_FOLDER


@routes_blueprint.route("/", methods=["GET"])
@routes_blueprint.route("/about_me", methods=["GET"])
def about_me():

    return render_template(
        "about_me.html",
        title="About Me"
    )

@routes_blueprint.route("/MQP", methods=["GET"])
def MQP():

    return render_template(
        "MQP.html",
        title="Assistive Elbow Exoskeleton"
    )

@routes_blueprint.route("/oscilloscope", methods=["GET"])
def oscilloscope():

    return render_template(
        "oscilloscope.html",
        title="Real-Time Oscilloscope"
    )


@routes_blueprint.route("/IQP", methods=["GET"])
def IQP():

    return render_template(
        "IQP.html",
        title="Designing a Course for Drone Piloting "
    )

@routes_blueprint.route("/RBE3001", methods=["GET"])
def RBE3001():
    return render_template(
        "RBE_3001.html",
        title="Programming a 4-DOF Robotic Arm"
    )

@routes_blueprint.route("/RBE3002", methods=["GET"])
def RBE3002():
    return render_template(
        "RBE_3002.html",
        title="Maze Running Robot"
    )

@routes_blueprint.route("/ECE4902", methods=["GET"])
def ECE4902():
    return render_template(
        "ECE_4902.html",
        title="Design of an Analog Operational Amplifier "
    )

@routes_blueprint.route("/RBE2001", methods=["GET"])
def RBE2001():
    return render_template(
        "RBE_2001.html",
        title="Mini Solar Panel Replacement Robot"
    )

@routes_blueprint.route("/Explorator", methods=["GET"])
def Explorator():
    return render_template(
        "Explorator.html",
        title="Explorator"
    )

@routes_blueprint.route("/Persephone", methods=["GET"])
def Persephone():
    return render_template(
        "Persephone.html",
        title="Persephone"
    )

@routes_blueprint.route("/Siemens", methods=["GET"])
def Siemens():
    return render_template(
        "Siemens.html",
        title="Siemens"
    )

@routes_blueprint.route("/Micross", methods=["GET"])
def Micross():
    return render_template(
        "Micross.html",
        title="Micross"
    )