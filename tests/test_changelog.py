from opprelease.changelog import automation_link, _process_doc_label


def test_automation_link():
    assert automation_link("automation.mqtt", False) == (
        "[automation.mqtt docs]: "
        "https://www.open-peer-power.io/docs/automation/trigger/#mqtt-trigger"
    )

    assert automation_link("automation.openpeerpower", False) == (
        "[automation.openpeerpower docs]: "
        "https://www.open-peer-power.io/docs/automation/trigger/"
        "#open-peer-power-trigger"
    )

    assert automation_link("automation.numeric_state", False) == (
        "[automation.numeric_state docs]: "
        "https://www.open-peer-power.io/docs/automation/trigger/"
        "#numeric-state-trigger"
    )


def test_process_doc_label():
    links = set()
    parts = []

    _process_doc_label("integration: hue", parts, links, False)

    assert parts[-1] == "([hue docs])"
    assert next(iter(links)).startswith("[hue docs]")
