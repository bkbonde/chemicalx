import unittest
import torch
from chemicalx.data import DatasetLoader, BatchGenerator

from chemicalx.models import (
    CASTER,
    DPDDI,
    EPGCNDS,
    GCNBMP,
    MHCADDI,
    MRGNN,
    SSIDDI,
    AUDNNSynergy,
    DeepCCI,
    DeepDDI,
    DeepDDS,
    DeepDrug,
    DeepSynergy,
    MatchMaker,
)


class TestModels(unittest.TestCase):
    def setUp(self):
        loader = DatasetLoader("drugcomb")
        drug_feature_set = loader.get_drug_features()
        context_feature_set = loader.get_context_features()
        labeled_triples = loader.get_labeled_triples()
        self.generator = BatchGenerator(
            batch_size=5120, context_features=True, drug_features=True, drug_molecules=True, labels=True
        )
        self.generator.set_data(context_feature_set, drug_feature_set, labeled_triples)

    def test_CASTER(self):
        model = CASTER(x=2)
        assert model.x == 2

    def test_DPDDI(self):
        model = DPDDI(x=2)
        assert model.x == 2

    def test_EPGCNDS(self):
        model = EPGCNDS(x=2)
        assert model.x == 2

    def test_GCNBMP(self):
        model = GCNBMP(x=2)
        assert model.x == 2

    def test_MHCADDI(self):
        model = MHCADDI(x=2)
        assert model.x == 2

    def test_MRGNN(self):
        model = MRGNN(x=2)
        assert model.x == 2

    def test_SSIDDI(self):
        model = SSIDDI(x=2)
        assert model.x == 2

    def test_AUDNNSynergy(self):
        model = AUDNNSynergy(x=2)
        assert model.x == 2

    def test_DeepCCI(self):
        model = DeepCCI(x=2)
        assert model.x == 2

    def test_DeepDDI(self):
        model = DeepDDI(x=2)
        assert model.x == 2

    def test_DeepDrug(self):
        model = DeepDrug(x=2)
        assert model.x == 2

    def test_DeepSynergy(self):

        model = DeepSynergy(
            context_channels=64,
            drug_channels=32,
            input_hidden_channels=32,
            middle_hidden_channels=16,
            final_hidden_channels=16,
            dropout_rate=0.5,
        )

        optimizer = torch.optim.Adam(model.parameters(), lr=0.01, weight_decay=0.0001)
        loss = torch.nn.BCELoss()
        for batch in self.generator:
            optimizer.zero_grad()
            prediction = model(batch.context_features, batch.drug_features_left, batch.drug_features_right)
            output = loss(prediction, batch.labels)
            output.backward()
            optimizer.step()

    def test_DeepDDS(self):
        model = DeepDDS(x=2)
        assert model.x == 2

    def test_MatchMaker(self):
        model = MatchMaker(x=2)
        assert model.x == 2
