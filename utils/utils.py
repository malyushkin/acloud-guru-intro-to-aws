import yaml

"""
Templates
* _H - headers
"""
TITLE_H = "# {title}\n"
SECTION_H = "\n## {title}\n"
SUBSECTION_H = "1. {title}\n"


def write_info(yml, name="README", ext="md"):
    with open(f"../{name}.{ext}", "w") as inf:
        # Write title
        inf.write(TITLE_H.format(title=yml["title"]))

        for section in yml["content"]:
            # Write section
            inf.write(SECTION_H.format(title=section["title"]))

            for subsection in section["content"]:
                # Write subsection
                inf.write(SUBSECTION_H.format(title=subsection["title"]))


if __name__ == "__main__":
    with open("course.yml", "r") as yml:
        try:
            data = yaml.safe_load(yml)
        except yaml.YAMLError as exception:
            raise exception

    write_info(data)
