from xml.etree import ElementTree as et


def parse_pom(filename):
    """Parses pom to figure identify artifact and version"""
    xml_ns = "http://maven.apache.org/POM/4.0.0"
    tree = et.ElementTree()
    tree.parse(filename)
    artifact = version = ""

    artifact_id = tree.getroot().find("{%s}artifactId" % xml_ns)
    if artifact_id is not None:
        artifact = artifact_id.text

    proj_version = tree.getroot().find("{%s}version" % xml_ns)
    if proj_version is not None:
        version = proj_version.text
    else:
        parent = tree.getroot().find("{%s}parent" % xml_ns)
        if parent:
            proj_version = parent.find("{%s}version" % xml_ns)
            if proj_version is not None:
                version = proj_version.text
    return artifact, version


def get_jar_filename(jar_path, artifact, version):
    return "{0}/{1}-{2}.jar".format(jar_path, artifact, version)
