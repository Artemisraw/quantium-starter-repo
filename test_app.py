import pytest
from dash import Dash
from app import app


def dash_duo_app():
    return app


def test_update_graph(dash_duo):

    # start the Dash app
    dash_duo.start_server(app)

    # load the page
    dash_duo.wait_for_element('#line-chart', timeout=10)

    # check if the app loaded succesfully
    assert dash_duo.find_element("#line-chart"), "Line chart did not render!"

    # check if the default graph is displayed
    graph = dash_duo.find_element("#line-chart")
    assert graph is not None, "Default graph not rendered correctly"

    # Check default radio value
    radio_items = dash_duo.find_element("#location")
    print(f"selected Items:{radio_items.text}")
    assert "All" in radio_items.text, "Default selection in radio items is incorrect"
    assert "North" in radio_items.text, "location does not exists"
    assert "South" in radio_items.text, "location does not exists"
    assert "East" in radio_items.text, "location does not exists"
    assert "West" in radio_items.text, "location does not exists"


    logs = dash_duo.get_logs()
    print("Browser Logs:", logs)


# Run test with pytest
if __name__ == "__main__":
    pytest.main()
