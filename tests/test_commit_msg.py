import check_commit_msg as cm


def test_mensaje_valido():
    assert cm.validar("feat(front): agrega pestaña de ayuda (#4)") == []


def test_cuerpo_con_closes():
    assert cm.validar("fix(back): corrige umbral\n\nCloses #7") == []


def test_clave_de_jira():
    assert cm.validar("chore: actualiza dependencias BIL-12") == []


def test_sin_tipo():
    assert cm.validar("cambios varios (#1)")


def test_sin_referencia_a_tarea():
    assert any("tarea" in e for e in cm.validar("feat: algo nuevo"))


def test_tipo_desconocido():
    assert cm.validar("update: cambia cosas (#3)")


def test_merge_exento():
    assert cm.validar("Merge branch 'main' into dev") == []
