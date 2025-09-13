import pytest

from playwright.sync_api import sync_playwright


# Si el scope = session se inicializa solo una vez y termina de ejecutar solo una vez
# Si el scope es vacio va inicializar en el test case cada vez que lo requiera y se va a cerrar

@pytest.fixture(scope="session")
def browser():
    print("Aqui comienza el fixture browser")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()
    print("Aqui termina el fixture browser")


#Opcion 1 : (scope = session) Va inicializar solo una vez el fixture en la pagina y los va a
#  cerrar una vez al terminar de ejecutar todos los test cases

# Se usa este tipo de scope = sesion cuando es muy requerido en la mayoria de los test cases

#@pytest.fixture(scope="session") 
#def page(browser):
#    print("Aqui comienza el fixture page")
#    context = browser.new_context()
#    page = context.new_page()       
#    yield page
#    context.close()
#    print("Aqui termina el fixture page")


#Opcion 2 : (scope = vacio) Va inicializar cada vez que se este usando en el test case y se va cerrar 
# solo si este se deja de usar en la ejecucion y va a volver a inicializar nuevamente 
# el fixture cuando se requiera usar en el test case siguiente eso implica que inicializa a cada rato 
# cuando se lo requiera en el test case y cierra el fixture si este ya no se esta utilizando

# Se usa este tipo de scope =  vacio cuando no es muy usado en los test cases

@pytest.fixture() 
def page(browser):
    print("Aqui comienza el fixture page")
    context = browser.new_context()
    page = context.new_page()       
    yield page
    context.close()
    print("Aqui termina el fixture page")



#@pytest.fixture(scope="session")
#@pytest.fixture
#def five():
    #print("Aqui comienza el fixture 5")
#    number=5
#    yield number 
#    number = 0
    #print("Aqui termina el fixture 5")

#@pytest.fixture
#def two():
#    return 5


#@pytest.fixture
#def array():
    #("Aqui comienza el fixture array")
#    arr = [1,2,3,4]
#    yield arr
#    arra = []
    #print("Aqui termina el fixture array")


#@pytest.fixture
#def multi_2():
    #print("Aqui comienza el fixture multi 2")
 #   number=2
 #   yield number 
 #   number = 0
    #print("Aqui termina el fixture multi 2")




    