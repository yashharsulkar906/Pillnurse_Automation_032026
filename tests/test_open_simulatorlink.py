def test_simulator_link(page):
    page.goto("https://staging.d2kcjp2bs55j6j.amplifyapp.com/")
    assert "amplifyapp.com" in page.url.lower()
    
    

    