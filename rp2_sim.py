def asm_pio(*args, **kwargs):
    #función decorador
    def decorador(programa):
        def compilador():
            print("Parámetros", kwargs)
            programa()
            return None
        return compilador
    return decorador

def decorador_instr(fun_inst):
    #función decorador sin retorno
    def decoracion_instr(self,*args, **kwargs):
        fun_inst(self,*args, **kwargs)
        return None
    return decoracion_instr

pins='pins'

class PIO():
    OUT_LOW='PIO.OUT_LOW'


class StateMachine:
     #funcion iniciadora
  def __init__(self, id_, program, freq=125000000, **kwargs):
         global sm_iniciandose,fsms
        sm_iniciandose=self
        #print('StateMachine.__init__',id_, program, freq, kwargs)
        self.lista_instr=[]
        program()
        print('Fueron leidas',len(self.lista_instr), 'instrucciones')
        sm_iniciandose=None
        fsms[id_]=self
        pass

#esta funcion simula La maquina de estados finitos
  def active(self, x=None):
    '''Esta rutina simula exclisivamnte esa FSM. Sería interesante crear simulación en parlelo con otras FSM'''
    #Simula FMS
    if x==1:
        print('Está pendiente de realizar la simulacón')

fsms=[None]*8

sm_iniciandose=None


class nop:
    @decorador_instr
    #esta funcion decora la funcion __init__
    def __init__(self,*args, **kwargs):
        global sm_iniciandose
        print(self.__class__.__name__)#,'nop.__init__',args,kwargs)
        sm_iniciandose.lista_instr.append(self)

        pass
#esta funcion llama al item name
    def __getitem__(self,name):
        #print('nop.__getattr__',name)
        pass

class set(nop):
    #esta funcion realiza un set a __init__
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        pass

class wrap_target(nop):
    #esta función envuelte el objetivo
    def __init__(self,*args, **kwargs):
         super().__init__(*args, **kwargs)
         pass

class wrap(nop):
    #esta funcion envuelve
    def __init__(self,*args, **kwargs):
         super().__init__(*args, **kwargs)
         pass
