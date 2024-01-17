from django.shortcuts import render
from .models import Area
from django.db.models import Q

def areas(request):
    # Todos as áreas
    todas_areas = Area.objects.all() #mesma coisa do 'select * from areas'
    
    # Id da área Informática
    area_info = Area.objects.get(nome='Informática') # 'get' Retorna apenas 1 objeto
    #area_info = Area.objects.filter(nome='Informática')  => 'filter' retorna varios objetos

    # Áreas que começam com a letra 'E'
    area_e = Area.objects.filter(nome__startswith='E')

    # Áreas que terminam com as letras 'ica'
    area_ica = Area.objects.filter(nome__endswith='ica')

    # Áreas que possuem o trecho 'mec'
    area_mec = Area.objects.filter(nome__contains='mec')

    # Áreas que possuem o trecho 'mec' e iniciam com 'Ele (opcao1)
    era_mec_ele = Area.objects.filter(nome__contains='mec',nome__startswith='Ele')

    # Áreas que possuem o trecho 'mec' e iniciam com 'Ele (opcao2)
    era_mec_ele_2 = Area.objects.filter(nome__contains='mec').filter(nome__startswith='Ele')

    # Áreas que possuem id 1 ou id 3
    area_1_3 = Area.objects.filter(Q(id=1) | Q(id=3))

    #Áreas que possuem id 1 ou que termine com 'tos'
    area_1_tos = Area.objects.filter(Q(id=1) | Q(nome__endswith='tos'))

    #Quantas areas terminam com as letras 'ica' (opcao1)
    area_ica_quant = Area.objects.filter(nome__endswith= 'ica')

    #Quantas areas terminam com as letras 'ica' (opcao2)
    area_ica_qtd_2 = Area.objects.filter(nome__endswith= 'ica').count()


    #Imprimir cursos por ordem alfabética

    
    #Imprimir areas por ordem alfabética inversa8

    

    contexto = {
        'todas_areas': todas_areas,
        'area_info': area_info,
        'area_e': area_e,
        'area_ica': area_ica,
        'area_mec': area_mec,
        'era_mec_ele' : era_mec_ele,
        'era_mec_ele_2' : era_mec_ele_2,
        'area_1_3' : area_1_3,
        'area_1_tos': area_1_tos,
        'area_ica_qtd_2': area_ica_qtd_2,
        'area_ica_quant':area_ica_quant
        
    }
    return render(request, 'areas.html', contexto)



def publicos(request):
    # Todos os públicosljo


    # Id do público 'Discentes'


    # Públicos que começam com a letra 'D'


    # Públicos que possuem o trecho 'centes


    # Públicos que possuem id 1 ou possuem o trecho 'terno'


    contexto = {

    }
    return render(request, 'publicos.html', contexto)



def cursos(request):
    # Listar todos os cursos


    # Listar cursos em ordem alfabética


    # Listar cursos em ordem alfabética inversa


    # Listar dados do curso de Android


    # Listar cursos com menos de 50 vagas


    # Listar cursos com mais de 50 vagas


    #Listar cursos que possuem vagas entre 35 e 70 vagas


    # Listar cursos que iniciam apenas em 2023


    # Listar cursos que iniciam no mês de dezembro de 2022


    # Listar cursos que são da área de Informática


    # Listar cursos que são da área de Eletromecânica


    # Listar cursos que são voltados para o público Docentes


    # Listar cursos que são voltados para o público Externo


    # Listar cursos que são voltados para o público Docentes e Discentes


    # Listar cursos que são voltados para o público Docentes ou Discentes


    # Listar cursos da área de Informática e que são voltados para o público Externo


    # Listar cursos da área de Informática, que são voltados para o público Discentes e que possuam mais de 40 vagas


    # Quantidade de cursos que são da área de Informática


    # Quantidade de cursos que são voltados para o público externo


    # Quantidade de cursos que são da área de Eventos e voltados para o público externo

    
    
    contexto = {

    }
    return render(request, 'cursos.html', contexto)