const apparatus = {"nodes": ["<ViciValve coupling_valve>", "<Vessel phe>", "<Vessel leu>", "<Vessel dmf>", "<Vessel diea>", "<Vessel ala>", "<Vessel fmoc_pna_a>", "<Vessel syringe_6>", "<Vessel fmoc_lys_oh>", "<Vessel hatu>", "<VarianPump activator_pump>", "<Vessel fmoc_pna_g>", "<Vessel fmoc_pna_c>", "<Vessel pip>", "<ViciValve amino_valve>", "<VarianPump diea_pump>", "<TMixer mixer>", "<Vessel fmoc_pna_t>", "<VarianPump amino_pump>"], "edges": [{"source": "<Vessel hatu>", "target": "<ViciValve coupling_valve>"}, {"source": "<Vessel dmf>", "target": "<ViciValve coupling_valve>"}, {"source": "<Vessel pip>", "target": "<ViciValve coupling_valve>"}, {"source": "<ViciValve coupling_valve>", "target": "<VarianPump activator_pump>"}, {"source": "<VarianPump activator_pump>", "target": "<TMixer mixer>"}, {"source": "<Vessel fmoc_pna_a>", "target": "<ViciValve amino_valve>"}, {"source": "<Vessel fmoc_pna_t>", "target": "<ViciValve amino_valve>"}, {"source": "<Vessel fmoc_pna_c>", "target": "<ViciValve amino_valve>"}, {"source": "<Vessel fmoc_pna_g>", "target": "<ViciValve amino_valve>"}, {"source": "<Vessel fmoc_lys_oh>", "target": "<ViciValve amino_valve>"}, {"source": "<Vessel syringe_6>", "target": "<ViciValve amino_valve>"}, {"source": "<Vessel ala>", "target": "<ViciValve amino_valve>"}, {"source": "<Vessel leu>", "target": "<ViciValve amino_valve>"}, {"source": "<Vessel phe>", "target": "<ViciValve amino_valve>"}, {"source": "<Vessel dmf>", "target": "<ViciValve amino_valve>"}, {"source": "<ViciValve amino_valve>", "target": "<VarianPump amino_pump>"}, {"source": "<VarianPump amino_pump>", "target": "<TMixer mixer>"}, {"source": "<Vessel diea>", "target": "<VarianPump diea_pump>"}, {"source": "<VarianPump diea_pump>", "target": "<TMixer mixer>"}]}

export default () => {
      return (apparatus);
}