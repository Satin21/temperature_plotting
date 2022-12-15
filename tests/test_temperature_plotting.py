import pytest
import temperature_plotting as tpl
import os

@pytest.mark.skip(reason='bad test')
def test_compute_mean():
    calc = tpl.compute_mean([0, 10, 20])
    assert calc == 9
    assert isinstance(calc, float)

    with pytest.raises(TypeError):
        calc = tpl.compute_mean(["a", "b", "c"])

def test_main():
    tpl.main()
    assert os.path.exists("plot_25.png")
